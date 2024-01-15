
from Model.DataBaseModel import ScanNetLocalDataBase
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time
import matplotlib.pyplot as plt

#Класс обновляет и подсчитывает статистику в реальном времени по буферу пакетов
class FlowsUpdate(QThread):
    view = None
    isRun = True
    def __init__(self, view = None):
        super().__init__()
        self.view = view

    def run(self):
        while (self.isRun==True):
           time.sleep(10)
           db = ScanNetLocalDataBase()
           flows = db.getFlows()
           while self.view.ui.tableWidget_3.rowCount() > 0:
              self.view.ui.tableWidget_3.removeRow(0)
           for flow in flows:
              self.view.insertFlows(flow)
    def stop(self):
        self.isRun = False


class RTStatsModel(QThread):
    #stats
    buf_packets = []
    totalBytes = 0
    bytesPerSec = 0
    totalBytesRecv = 0
    totalBytesSend = 0
    totalPacketsSend = 0
    totalPacketsRecv = 0
    totalPackets = 0
    db = ScanNetLocalDataBase()
    finished = pyqtSignal()
    x = 0
    #график количества байт
    ox = []
    oy = []
    #частотный анализ ip
    ips = []
    unique_ips = set()
    ox1 = []
    oy1 = []
    #count_packets
    count_packets = []
    time_packets = []


    view = None
    def __init__(self, view = None, buf_packet = None):
        super().__init__()
        self.view = view
        self.buf_packets = buf_packet


    # Общее количество полученых пакетов в байтах

    def totalBytesUpdate(self, new_buf_packets):
        self.totalPackets += len(new_buf_packets)
        for packet in new_buf_packets:
            bytes = packet[6]
            self.totalBytes += bytes

            if(packet[1]!="192.168.0.101"):
                self.totalBytesRecv += bytes
                self.totalPacketsSend += 1
            else:
                self.totalBytesSend += bytes
                self.totalPacketsRecv += 1
        self.view.ui.textTotalBytes_5.setText(str(self.totalPackets))
        self.view.ui.textTotalBytes_6.setText(str(self.totalPacketsSend))
        self.view.ui.textTotalBytes_7.setText(str(self.totalPacketsRecv))
        self.view.ui.textTotalBytes_3.setText(str(self.totalBytesRecv) + " bytes")
        self.view.ui.textTotalBytes_4.setText(str(self.totalBytesSend) + " bytes")
        self.view.ui.textTotalBytes.setText(str(self.totalBytes) + " bytes")

        # print(self.totalBytes)
    def drawBytesPerSec(self, new_buf_packets):
        bytesPerSec = 0
        self.x += 1
        self.count_packets.append(len(new_buf_packets))
        self.ox.append(self.x)
        for packet in new_buf_packets:
            bytesPerSec += packet[6]

        self.oy.append(bytesPerSec)
        self.bytesPerSec = bytesPerSec
        self.view.ui.textTotalBytes_2.setText(str(self.bytesPerSec) + " bytes/sec")

    def countuniqips(self):
        #self.ox1.clear()
        #self.oy1.clear()

        plt.xticks(rotation=90)
        plt.bar(self.ox1, self.oy1)
        plt.savefig("ips.png")
        plt.clf()


    def run(self):
        print("Run!")
        while True:
           time.sleep(0.001)
           if(self.x%25==0):
               self.view.loadimage("bytes_s.png",0)
               self.view.loadimage("packets.png",1)
               self.view.loadimage("most_ips.png",2)
               self.view.loadimage("protos_pie.png",3)
               #self.countuniqips()

           if len(self.buf_packets)>0:
             self.totalBytesUpdate(self.buf_packets)
             self.drawBytesPerSec(self.buf_packets)

           for packet_data in self.buf_packets:
               self.db.insertPacket(str(packet_data[0]), packet_data[8], packet_data[9], packet_data[1],packet_data[2],packet_data[7],packet_data[6], str(packet_data[0].year), str(packet_data[0].microsecond), packet_data[4], packet_data[5], packet_data[3])
               self.view.insertPacket(packet_data)
           self.buf_packets.clear()
           self.finished.emit()
    def setBufPacket(self,new_buf_packets):
        self.buf_packets = new_buf_packets