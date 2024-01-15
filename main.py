from PyQt5.QtWidgets import QApplication
import sys
from View import View, MapView
from Model import Model
from Controller import Controller
from Model.DataBaseModel import ScanNetLocalDataBase

if __name__ == '__main__':

      app = QApplication(sys.argv)

      db = ScanNetLocalDataBase()
      db.clearDB()
      db.createDataBase("scannet.db")
     # ports,count = db.getPortsCount()
     # plt.xticks(rotation=90)
     # bar_colors = ['tab:blue' ,'tab:red', 'tab:blue', 'tab:red', 'tab:orange']
     # plt.bar(ports, count, color=bar_colors, alpha=0.7)
     # plt.tight_layout()
     # plt.savefig("most_ports.png")
     # plt.clf()
     # plt.close()
      #db.insertPacket("1", "src_mac", "dest_mac", "0")


      #th = threading.Thread(target=netio)
      #th.start()

      #while True:
         #pk = sniff(count=1)
         #print(pk.getlayer(n))

      controller = Controller.Controller()
      view = View.View(controller)
      controller.view = view
      controller.mapview = MapView.MapView()

      view.initMainUI()

      sys.exit((app.exec_()))

