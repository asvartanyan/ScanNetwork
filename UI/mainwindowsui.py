# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\mainwindowsui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 822)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 971, 801))
        self.tabWidget.setObjectName("tabWidget")
        self.capture_tab = QtWidgets.QWidget()
        self.capture_tab.setObjectName("capture_tab")
        self.label_curr_interface = QtWidgets.QLabel(self.capture_tab)
        self.label_curr_interface.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.label_curr_interface.setObjectName("label_curr_interface")
        self.listWidget_2 = QtWidgets.QListWidget(self.capture_tab)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 30, 871, 81))
        self.listWidget_2.setObjectName("listWidget_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.capture_tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 160, 881, 601))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.start_pushButton = QtWidgets.QPushButton(self.capture_tab)
        self.start_pushButton.setEnabled(True)
        self.start_pushButton.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.start_pushButton.setCheckable(False)
        self.start_pushButton.setObjectName("start_pushButton")
        self.stop_pushButton = QtWidgets.QPushButton(self.capture_tab)
        self.stop_pushButton.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.capture_tab)
        self.textEdit.setGeometry(QtCore.QRect(450, 120, 351, 31))
        self.textEdit.setDocumentTitle("")
        self.textEdit.setObjectName("textEdit")
        self.settingTable_toolButton = QtWidgets.QToolButton(self.capture_tab)
        self.settingTable_toolButton.setGeometry(QtCore.QRect(900, 160, 51, 31))
        self.settingTable_toolButton.setObjectName("settingTable_toolButton")
        self.apply_pushButton = QtWidgets.QPushButton(self.capture_tab)
        self.apply_pushButton.setGeometry(QtCore.QRect(810, 130, 75, 23))
        self.apply_pushButton.setObjectName("apply_pushButton")
        self.saveToFile_pushButton = QtWidgets.QPushButton(self.capture_tab)
        self.saveToFile_pushButton.setGeometry(QtCore.QRect(210, 130, 75, 23))
        self.saveToFile_pushButton.setObjectName("saveToFile_pushButton")
        self.time_record = QtWidgets.QLabel(self.capture_tab)
        self.time_record.setGeometry(QtCore.QRect(0, 760, 47, 13))
        self.time_record.setObjectName("time_record")
        self.tabWidget.addTab(self.capture_tab, "")
        self.endpoints_tab = QtWidgets.QWidget()
        self.endpoints_tab.setObjectName("endpoints_tab")
        self.UpdatePushButton = QtWidgets.QPushButton(self.endpoints_tab)
        self.UpdatePushButton.setGeometry(QtCore.QRect(680, 20, 111, 23))
        self.UpdatePushButton.setObjectName("UpdatePushButton")
        self.OpenMapPushButton = QtWidgets.QPushButton(self.endpoints_tab)
        self.OpenMapPushButton.setGeometry(QtCore.QRect(680, 50, 111, 23))
        self.OpenMapPushButton.setObjectName("OpenMapPushButton")
        self.listWidget = QtWidgets.QListWidget(self.endpoints_tab)
        self.listWidget.setGeometry(QtCore.QRect(30, 450, 341, 261))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.tableWidget = QtWidgets.QTableWidget(self.endpoints_tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 641, 431))
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.endpoints_tab, "")
        self.analyze_tab = QtWidgets.QWidget()
        self.analyze_tab.setObjectName("analyze_tab")
        self.qlabel = QtWidgets.QLabel(self.analyze_tab)
        self.qlabel.setGeometry(QtCore.QRect(10, 20, 471, 361))
        self.qlabel.setScaledContents(False)
        self.qlabel.setObjectName("qlabel")
        self.qlabel_2 = QtWidgets.QLabel(self.analyze_tab)
        self.qlabel_2.setGeometry(QtCore.QRect(490, 20, 471, 361))
        self.qlabel_2.setObjectName("qlabel_2")
        self.qlabel_3 = QtWidgets.QLabel(self.analyze_tab)
        self.qlabel_3.setGeometry(QtCore.QRect(10, 390, 471, 361))
        self.qlabel_3.setObjectName("qlabel_3")
        self.qlabel_4 = QtWidgets.QLabel(self.analyze_tab)
        self.qlabel_4.setGeometry(QtCore.QRect(490, 390, 471, 361))
        self.qlabel_4.setObjectName("qlabel_4")
        self.tabWidget.addTab(self.analyze_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.LabelTB = QtWidgets.QLabel(self.tab)
        self.LabelTB.setGeometry(QtCore.QRect(10, 20, 411, 41))
        self.LabelTB.setAutoFillBackground(True)
        self.LabelTB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LabelTB.setObjectName("LabelTB")
        self.textTotalBytes = QtWidgets.QLabel(self.tab)
        self.textTotalBytes.setGeometry(QtCore.QRect(110, 30, 291, 21))
        self.textTotalBytes.setObjectName("textTotalBytes")
        self.LabelTB_2 = QtWidgets.QLabel(self.tab)
        self.LabelTB_2.setGeometry(QtCore.QRect(10, 70, 411, 41))
        self.LabelTB_2.setAutoFillBackground(True)
        self.LabelTB_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LabelTB_2.setObjectName("LabelTB_2")
        self.textTotalBytes_2 = QtWidgets.QLabel(self.tab)
        self.textTotalBytes_2.setGeometry(QtCore.QRect(110, 80, 291, 21))
        self.textTotalBytes_2.setObjectName("textTotalBytes_2")
        self.LabelTB_3 = QtWidgets.QLabel(self.tab)
        self.LabelTB_3.setGeometry(QtCore.QRect(10, 120, 411, 41))
        self.LabelTB_3.setAutoFillBackground(True)
        self.LabelTB_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LabelTB_3.setObjectName("LabelTB_3")
        self.textTotalBytes_3 = QtWidgets.QLabel(self.tab)
        self.textTotalBytes_3.setGeometry(QtCore.QRect(110, 130, 291, 21))
        self.textTotalBytes_3.setObjectName("textTotalBytes_3")
        self.LabelTB_4 = QtWidgets.QLabel(self.tab)
        self.LabelTB_4.setGeometry(QtCore.QRect(10, 170, 411, 41))
        self.LabelTB_4.setAutoFillBackground(True)
        self.LabelTB_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LabelTB_4.setObjectName("LabelTB_4")
        self.textTotalBytes_4 = QtWidgets.QLabel(self.tab)
        self.textTotalBytes_4.setGeometry(QtCore.QRect(110, 180, 291, 21))
        self.textTotalBytes_4.setObjectName("textTotalBytes_4")
        self.LabelTB_5 = QtWidgets.QLabel(self.tab)
        self.LabelTB_5.setGeometry(QtCore.QRect(10, 220, 411, 41))
        self.LabelTB_5.setAutoFillBackground(True)
        self.LabelTB_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LabelTB_5.setObjectName("LabelTB_5")
        self.textTotalBytes_5 = QtWidgets.QLabel(self.tab)
        self.textTotalBytes_5.setGeometry(QtCore.QRect(110, 230, 291, 21))
        self.textTotalBytes_5.setObjectName("textTotalBytes_5")
        self.LabelTB_6 = QtWidgets.QLabel(self.tab)
        self.LabelTB_6.setGeometry(QtCore.QRect(10, 270, 411, 41))
        self.LabelTB_6.setAutoFillBackground(True)
        self.LabelTB_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LabelTB_6.setObjectName("LabelTB_6")
        self.textTotalBytes_6 = QtWidgets.QLabel(self.tab)
        self.textTotalBytes_6.setGeometry(QtCore.QRect(110, 280, 291, 21))
        self.textTotalBytes_6.setObjectName("textTotalBytes_6")
        self.LabelTB_7 = QtWidgets.QLabel(self.tab)
        self.LabelTB_7.setGeometry(QtCore.QRect(10, 320, 411, 41))
        self.LabelTB_7.setAutoFillBackground(True)
        self.LabelTB_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LabelTB_7.setObjectName("LabelTB_7")
        self.textTotalBytes_7 = QtWidgets.QLabel(self.tab)
        self.textTotalBytes_7.setGeometry(QtCore.QRect(110, 330, 291, 21))
        self.textTotalBytes_7.setObjectName("textTotalBytes_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(40, 30, 891, 681))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.listWidget_2.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_curr_interface.setText(_translate("MainWindow", "Current interface:"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source IP"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Destination IP"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "protocol"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "sPort"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "dPort"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Len"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "TTL"))
        self.start_pushButton.setText(_translate("MainWindow", "Start"))
        self.stop_pushButton.setText(_translate("MainWindow", "Stop"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "caputer filter"))
        self.settingTable_toolButton.setText(_translate("MainWindow", "..."))
        self.apply_pushButton.setText(_translate("MainWindow", "Apply"))
        self.saveToFile_pushButton.setText(_translate("MainWindow", "Save to file"))
        self.time_record.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.capture_tab), _translate("MainWindow", "Capture"))
        self.UpdatePushButton.setText(_translate("MainWindow", "Update"))
        self.OpenMapPushButton.setText(_translate("MainWindow", "Show on map"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Новый элемент"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IP"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Port"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Country"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "City"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.endpoints_tab), _translate("MainWindow", "Endpoints"))
        self.qlabel.setText(_translate("MainWindow", "TextLabel"))
        self.qlabel_2.setText(_translate("MainWindow", "TextLabel"))
        self.qlabel_3.setText(_translate("MainWindow", "TextLabel"))
        self.qlabel_4.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analyze_tab), _translate("MainWindow", "Analyze"))
        self.LabelTB.setText(_translate("MainWindow", "Total Bytes:"))
        self.textTotalBytes.setText(_translate("MainWindow", "TextLabel"))
        self.LabelTB_2.setText(_translate("MainWindow", "Bytes/Sec:"))
        self.textTotalBytes_2.setText(_translate("MainWindow", "TextLabel"))
        self.LabelTB_3.setText(_translate("MainWindow", "Bytes Recv:"))
        self.textTotalBytes_3.setText(_translate("MainWindow", "TextLabel"))
        self.LabelTB_4.setText(_translate("MainWindow", "Bytes Send:"))
        self.textTotalBytes_4.setText(_translate("MainWindow", "TextLabel"))
        self.LabelTB_5.setText(_translate("MainWindow", "Total packets:"))
        self.textTotalBytes_5.setText(_translate("MainWindow", "TextLabel"))
        self.LabelTB_6.setText(_translate("MainWindow", "Total Packet Send:"))
        self.textTotalBytes_6.setText(_translate("MainWindow", "TextLabel"))
        self.LabelTB_7.setText(_translate("MainWindow", "Total Packets Recv:"))
        self.textTotalBytes_7.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Stats"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Source IP"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Destination IP"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "sPort"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "dPort"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Count packets"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Flows"))
