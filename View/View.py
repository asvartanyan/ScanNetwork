import PyQt5.uic.uiparser
import numpy as np
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QTableView, QTableWidget)
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from Controller import Controller
from UI.mainwindowsui import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem, QLabel
from PyQt5.QtGui import QPixmap
from Model.CaptureModel import CaptureNetwork
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import sys
import time



class View(QMainWindow):
    controller = Controller.Controller()
    timer_update = QTimer()
    timer_packets = QTimer()
    timer_record_time = QTimer()
    timer_upd_stats = QTimer()
    def __init__(self, controller = None):
        super(View, self).__init__()
        self.controller = controller

        #self.worker.progress.connect(self.reportProgress)


    def initMainUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)


        self.setToolTip('This is a <b>QWidget</b> widget')

        #btn = QPushButton('Add +1', self)
        #btn.setToolTip('This is a <b>QPushButton</b> widget')
        #btn.resize(btn.sizeHint())
        #btn.move(50, 50)
        #btn.clicked.connect(self.controller.the_button_was_clicked)

        self.ui.UpdatePushButton.clicked.connect(self.controller.handle_update_list_button)
        self.timer_update.timeout.connect(self.controller.handle_timer_update)
        #self.timer_update.start(self.controller.update_time_endpoints)
        self.ui.OpenMapPushButton.clicked.connect(self.controller.handle_show_on_map)


        self.ui.listWidget_2.currentItemChanged.connect(self.controller.handle_update_current_interface)
        self.controller.handle_update_list_interfaces()
        self.ui.listWidget_2.setCurrentRow(0)


        self.ui.start_pushButton.clicked.connect(self.controller.handle_start_button_click)
        self.ui.stop_pushButton.clicked.connect(self.controller.handle_stop_button_click)
        #self.timer_packets.timeout.connect(self.controller.handle_timer_packets_update)
        self.timer_upd_stats.timeout.connect(self.controller.handle_stats_update)

        self.ui.apply_pushButton.clicked.connect(self.controller.handle_apply_button)
        self.statusBar().showMessage(str(0))


        #self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


    def initMapUI(self):
        self.setGeometry(500,500,500,500)
        self.move(300, 300)
        self.setWindowTitle('Simple')
        self.show()
    def loadimage(self,imagename, qlabeL = 0):
        pixmap = QPixmap(imagename)
        #self.ui.qlabel = QLabel(self)
        if (qlabeL == 0):
           self.ui.qlabel.setPixmap(pixmap)
        elif (qlabeL == 1):
            self.ui.qlabel_2.setPixmap(pixmap)
        elif (qlabeL == 2):
            self.ui.qlabel_3.setPixmap(pixmap)
        elif (qlabeL == 3):
            self.ui.qlabel_4.setPixmap(pixmap)
        #self.ui.qlabel.resize(pixmap.width(), pixmap.height())
        self.ui.qlabel.show()

    def updateRecordTime(self,starttime):
        self.statusBar().showMessage(str(f'Time: {time.time()-starttime}'))
    def insertPacket(self,packet_data):
        rowPosition = self.ui.tableWidget_2.rowCount()
        self.ui.tableWidget_2.insertRow(rowPosition)
        self.ui.tableWidget_2.setItem(rowPosition, 0, QTableWidgetItem(str(packet_data[0])))
        self.ui.tableWidget_2.setItem(rowPosition, 1, QTableWidgetItem(str(packet_data[1])))
        self.ui.tableWidget_2.setItem(rowPosition, 2, QTableWidgetItem(str(packet_data[2])))
        self.ui.tableWidget_2.setItem(rowPosition, 3, QTableWidgetItem(str(packet_data[3])))
        self.ui.tableWidget_2.setItem(rowPosition, 4, QTableWidgetItem(str(packet_data[4])))
        self.ui.tableWidget_2.setItem(rowPosition, 5, QTableWidgetItem(str(packet_data[5])))
        self.ui.tableWidget_2.setItem(rowPosition, 6, QTableWidgetItem(str(packet_data[6])))
        self.ui.tableWidget_2.setItem(rowPosition, 7, QTableWidgetItem(str(packet_data[7])))
        self.ui.tableWidget_2.scrollToBottom()

    def insertFlows(self, flows):
        rowPosition = self.ui.tableWidget_3.rowCount()
        self.ui.tableWidget_3.insertRow(rowPosition)
        self.ui.tableWidget_3.setItem(rowPosition, 0, QTableWidgetItem(str(flows[0])))
        self.ui.tableWidget_3.setItem(rowPosition, 1, QTableWidgetItem(str(flows[1])))
        self.ui.tableWidget_3.setItem(rowPosition, 2, QTableWidgetItem(str(flows[2])))
        self.ui.tableWidget_3.setItem(rowPosition, 3, QTableWidgetItem(str(flows[3])))
        self.ui.tableWidget_3.setItem(rowPosition, 4, QTableWidgetItem(str(flows[4])))
        self.ui.tableWidget_3.setItem(rowPosition, 5, QTableWidgetItem(str(flows[5])))
        self.ui.tableWidget_3.scrollToBottom()










