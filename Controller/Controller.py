import threading

import folium

from Model import Model
from Model.CaptureModel import CaptureNetwork, UpdateRecordTime
from Model.RTStatsModel import RTStatsModel, FlowsUpdate
from View import View, MapView
import time
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import matplotlib.pyplot as plt
from Model.DataBaseModel import ScanNetLocalDataBase

class Controller:
    model = Model.Model()
    rtstatsmodel = None
    totalBytes = 1
    view = None
    update_time_endpoints = 16000
    update_time_packets = 10
    update_time_stats = 1000
    mapview = None
    filter = ""

    packet = []
    packets = []
    times_now = 0
    count_packets = []
    count_time = []



    def __init__(self):
        self.thread = QThread()
        self.worker = CaptureNetwork()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.worker.deleteLater)

        self.threadRecordTime = QThread()
        self.workerRecord = UpdateRecordTime()
        self.workerRecord.moveToThread(self.threadRecordTime)
        self.threadRecordTime.started.connect(self.workerRecord.run)
        self.workerRecord.finished.connect(self.threadRecordTime.quit)
        self.workerRecord.finished.connect(self.workerRecord.deleteLater)
        self.threadRecordTime.finished.connect(self.workerRecord.deleteLater)

        self.rtsThread = QThread()
        self.workerUpdate = RTStatsModel()
        self.workerUpdate.moveToThread(self.rtsThread)
        self.rtsThread.started.connect(self.workerUpdate.run)
        self.workerUpdate.finished.connect(self.rtsThread.quit)
        self.workerUpdate.finished.connect(self.workerUpdate.deleteLater)
        self.rtsThread.finished.connect(self.workerUpdate.deleteLater)

        self.flowThread = QThread()
        self.workerFlow = FlowsUpdate()
        self.workerFlow.moveToThread(self.flowThread)
        self.flowThread.started.connect(self.workerFlow.run)
        self.workerFlow.finished.connect(self.flowThread.quit)
        self.workerFlow.finished.connect(self.workerFlow.deleteLater)
        self.flowThread.finished.connect(self.workerFlow.deleteLater)


    def the_button_was_clicked(self):
        self.model.increment()
        self.view.statusBar().showMessage(str(self.model.num))
        self.view.ui.tableWidget.horizontalHeader().setVisible(False)

    def handle_update_list_button(self):
        net_list = self.model.getNetConnectionList()
        self.view.ui.listWidget.clear()
        while self.view.ui.tableWidget.rowCount() > 0:
            self.view.ui.tableWidget.removeRow(0)
        for net in net_list:
            self.view.ui.listWidget.addItem(str(net))
            rowPosition = self.view.ui.tableWidget.rowCount()
            self.view.ui.tableWidget.insertRow(rowPosition)
            self.view.ui.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(net["ip"])))
            self.view.ui.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(net["port"])))
            self.view.ui.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(net["country"])))
            self.view.ui.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(net["city"])))



    def handle_timer_update(self):
        self.handle_update_list_button()
        self.model.packets = self.worker.packets
        print(self.worker.packets)
        self.view.timer_update.start(self.update_time_endpoints)

    #def handle_timer_packets_update(self):
        #self.handle_update_table_packets()
        #self.view.timer_packets.start(self.update_time_packets)

    def handle_show_on_map(self):
        _map = self.model.getFoliumMapWithMarkers(self.model.getNetConnectionList())
        self.mapview = MapView.MapView(_map)
        self.mapview.close()
        self.mapview.show()
    def handle_update_list_interfaces(self):
        interfaces = self.model.getListInterfaces()
        for inter_, val in zip(interfaces.keys(),interfaces.values()):
            self.view.ui.listWidget_2.addItem(val + " " + inter_)

    def handle_update_current_interface(self):


        current_inter = self.view.ui.listWidget_2
        print(self.view.ui.listWidget_2.currentIndex().row())
        i = self.view.ui.listWidget_2.currentIndex().row()
        self.model.current_interface_index = i
        self.model.updateNameCurrentInterface()
    def handle_start_button_click(self):

        starttime = time.time()

        print("go")

        self.clear_table_packets()

        self.view.ui.start_pushButton.setEnabled(False)
        self.view.ui.stop_pushButton.setEnabled(True)
        device = self.model.current_interface_name
        self.view.ui.tableWidget_2.rowCount()
        #self.thread.terminate()

        #self.view.timer_packets.start(self.update_time_packets)

        self.worker = CaptureNetwork(device, self.view, self.filter)

        self.workerRecord = UpdateRecordTime(self.view, starttime)
        self.workerUpdate = RTStatsModel(self.view,[])
        self.workerFlow = FlowsUpdate(self.view)
        print(self.worker.device)
        print("go1")
        #self.worker.moveToThread(self.thread)
        #self.thread.started.connect(self.worker.run)
        #self.worker.finished.connect(self.thread.quit)
        #self.worker.finished.connect(self.worker.deleteLater)
       # self.thread.finished.connect(self.worker.deleteLater)
        self.worker.start()
        self.workerRecord.start()
        self.workerUpdate.start()
        self.workerFlow.start()
        #self.worker.progress.connect(self.handle_stats_update)
        #self.rtstatsmodel = RTStatsModel(self.view)
        self.view.timer_upd_stats.start(self.update_time_stats)


    def handle_stats_update(self):
        print("PROGRESS!")
        self.times_now += 1
        self.count_time.append(self.times_now)

        buf_packet = self.worker.getbufpackets()[:100].copy()

        self.packets += buf_packet
        self.workerUpdate.buf_packets = buf_packet.copy()
        print(len(buf_packet))

        self.count_packets.append(len(buf_packet))

        print(len(self.packets))
        self.analytisc()
        self.analyticsIP()
        self.analyticsProto()
        self.analyticsPackets()
        self.view.timer_upd_stats.start(self.update_time_stats)
        #self.rtstatsmodel.setBufPacket(buf_packet)
       # self.rtstatsmodel.startStats()

    def analytisc(self):
        plt.figure(figsize=(4, 3))
        plt.plot(self.workerUpdate.ox, self.workerUpdate.oy)
        plt.xlabel('time (s)')
        plt.ylabel('bytes')
        plt.tight_layout()
        plt.fill_between(self.workerUpdate.ox, self.workerUpdate.oy, color='lightblue', alpha=0.5)
        plt.savefig("bytes_s.png")
        plt.clf()
        plt.close()
    def analyticsIP(self):
        plt.figure(figsize=(4, 3))
        db = ScanNetLocalDataBase()
        ips, count = db.getIPcounts()
        plt.xticks(rotation=90)
        plt.bar(ips, count)
        plt.tight_layout()
        plt.savefig("most_ips.png")
        plt.clf()
        plt.close()
    def analyticsProto(self):
        plt.figure(figsize=(4, 3))
        db = ScanNetLocalDataBase()
        protos, count = db.getProtosCount()
        print(protos)
        print(count)
        plt.pie(count, labels=protos, autopct='%1.1f%%')
        plt.tight_layout()
        plt.savefig("protos_pie.png")
        plt.clf()
        plt.close()
    def analyticsPackets(self):
        plt.figure(figsize=(4, 3))
        plt.plot(self.count_time, self.count_packets)
        plt.xlabel('time (s)')
        plt.ylabel('packets')
        plt.fill_between(self.count_time, self.count_packets, color='lightblue', alpha=0.5)
        plt.tight_layout()
        plt.savefig("packets.png")
        plt.clf()
        plt.close()

    def handle_stop_button_click(self):
        self.view.timer_upd_stats.stop()
        self.workerFlow.stop()
        self.view.ui.start_pushButton.setEnabled(True)
        self.view.ui.stop_pushButton.setEnabled(False)
        self.rtstatsmodel = None
        #self.thread.run()
        #self.thread.terminate()
        #self.thread.quit()
        #del(self.thread)
        #self.thread = QThread()
        #self.thread.terminate()
        #self.thread.join()


        self.worker.stop_scan()
        self.workerRecord.stop1()
        self.workerStats = None

        #self.worker.quit()
        self.worker = None
        self.workerRecord = None
        #self.worker.deleteLater()

        #self.thread.terminate()
        #self.worker.finished
        #print(self.worker.)

       # self.thread.deleteLater()
        self.thread.quit()
        print(self.thread.isFinished())
        self.threadRecordTime.quit()
        self.rtstatsmodel = None
        #self.thread.join()

        #del(self.thread)
        #del self.thread
        #self.stop_thread_signal.emit()
        #self.model.stopCapture()
        #self.view.timer_packets.stop()
    def handle_update_table_packets(self):
        while self.view.ui.tableWidget_2.rowCount() > 0:
            self.view.ui.tableWidget_2.removeRow(0)
        for packet in self.model.packets:
            rowPosition = self.view.ui.tableWidget_2.rowCount()
            self.view.ui.tableWidget_2.insertRow(rowPosition)
            self.view.ui.tableWidget_2.setItem(rowPosition, 0, QTableWidgetItem(str(rowPosition)))
            self.view.ui.tableWidget_2.setItem(rowPosition, 1, QTableWidgetItem(str(packet[0])))
            self.view.ui.tableWidget_2.setItem(rowPosition, 2, QTableWidgetItem(str(packet[1])))
            self.view.ui.tableWidget_2.setItem(rowPosition, 3, QTableWidgetItem(str(packet[2])))
            self.view.ui.tableWidget_2.setItem(rowPosition, 4, QTableWidgetItem(str(packet[3])))
            self.view.ui.tableWidget_2.setItem(rowPosition, 5, QTableWidgetItem(str(packet[4])))
        self.view.ui.tableWidget_2.scrollToBottom()
    def clear_table_packets(self):
        while self.view.ui.tableWidget_2.rowCount() > 0:
            self.view.ui.tableWidget_2.removeRow(0)
    def handle_apply_button(self):
        self.filter = self.view.ui.textEdit.toPlainText()
    def update_time_timer(self):
        self.view.timer_record_time.start(self.update_time_endpoints)
        self.view.time_record.text()

















