import socket
import struct
import threading

import scapy.layers.inet
from winpcapy import WinPcapUtils, WinPcapDevices, WinPcap
import dpkt.ethernet
import dpkt.utils
from scapy.utils import hexdump
from scapy.all import sniff
from scapy.all import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import pyqtSignal

from Model.DataBaseModel import ScanNetLocalDataBase
import time

class UpdateRecordTime(QThread):
    starttime = None
    view = None
    isRun = True
    def __init__(self, view = None,stattime=None):
        super().__init__()
        self.starttime = stattime
        self.view = view
        self.isRun = True
    def run(self):

        while self.isRun:
            time.sleep(0.001)
            self.view.updateRecordTime(self.starttime)
    def stop1(self):
        self.isRun = False



class CaptureNetwork(QThread):
    packets = []
    device = "\\Device\\NPF_{122E0F47-8214-4AA7-9C2A-09916E9FC15E}"
    finished = pyqtSignal()
    progress = pyqtSignal()
    isRun = True
    filter = ""
    buf_packets = []
    ex_b_p = []
    bandwidth = 1


    def __init__(self,device=None, view = None, filter = None):
        super().__init__()
        self.device = device
        self.isRun = True
        self.view = view
        self.filter = filter

    def run(self):
        self.isRun = True

        print("Thread ")

        if (os.name == "n1t"):
            while (self.isRun == True):
                #self.progress.emit()
                with WinPcap(self.device, promiscuous=1) as capture:
                    capture.run(callback=self.packet_callback1, limit=self.bandwidth)
                    if (self.isRun == False):
                        capture.stop()


        else:
            while(self.isRun==True):
                sniff(iface=self.device, prn=self.packetcallback,  filter=self.filter)
                #self.progress.emit()

        #self.progress.emit(1)
        #self.finished.emit()

    def stop_scan(self):
        print("Stop")
        self.isRun = False
        #self.finished.emit()
    def getbufpackets(self):
        bufpckts = self.buf_packets.copy()#self.buf_packets[len(self.buf_packets)-self.bandwidth:].copy()
        self.buf_packets.clear()
        return bufpckts
    #Обработка одного пакета и добавление его в общий буфер
    def packetcallback(self, packet):
        #print(packet.show())
        proto = "Unknown"
        sport = ""
        dport = ""
        smac = ""
        dmac = ""
        if packet.haslayer(scapy.layers.inet.Ether):
            smac = packet[scapy.layers.inet.Ether].src
            dmac = packet[scapy.layers.inet.Ether].dst
        if packet.haslayer(scapy.layers.inet.IP):
           if packet.haslayer(scapy.layers.inet.TCP):
              proto = "TCP"
              sport = packet[scapy.layers.inet.TCP].sport
              dport = packet[scapy.layers.inet.TCP].dport
           if packet.haslayer(scapy.layers.inet.UDP):
              proto = "UDP"
              sport = packet[scapy.layers.inet.UDP].sport
              dport = packet[scapy.layers.inet.UDP].dport
           packet_data = [datetime.now(),
                          packet[scapy.layers.inet.IP].src,
                          packet[scapy.layers.inet.IP].dst,
                          str(proto),
                          sport,
                          dport,
                          packet[scapy.layers.inet.Ether].len,
                          packet[scapy.layers.inet.IP].ttl,
                          smac,
                          dmac
                          ]
           print(packet_data)
           self.buf_packets.append(packet_data)



    def packet_callback1(self,win_pcap, param, header, pkt_data):
        #packet_data = [datetime.now(), packet[scapy.layers.inet.IP].src, packet[scapy.layers.inet.IP].dst,
                       #packet[scapy.layers.inet.Ether].len, packet[scapy.layers.inet.IP].ttl, 0]
        ip_frame = pkt_data
        #print(ip_frame)
        eth = dpkt.ethernet.Ethernet(ip_frame)
        ip = eth.data

        dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', pkt_data[:14])

        packet = [datetime.now(), dpkt.utils.inet_to_str(ip.src), dpkt.utils.inet_to_str(ip.dst), len(ip_frame), ip.ttl, ip.df, ip.mf,
                  ip.offset]

        self.buf_packets.append(packet)


    def packet_callback(self, win_pcap, param, header, pkt_data):
        # Assuming IP (for real parsing use modules like dpkt)
        print(len(pkt_data))
        ip_frame = pkt_data
        ip = eth.data

        print(hexdump(pkt_data))

        print(pkt_data[:14], ip_frame[:14])
        dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', pkt_data[:14])
        #if not isinstance(eth.data, dpkt.ip.IP):
            #print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)

        print(socket.htons(proto))
        # Parse ips
        # print(ip_frame)
        # src_ip = ".".join([str(ord(b)) for b in ip_frame[0xc:0x10]])
        # dst_ip = ".".join([str(ord(b)) for b in ip_frame[0x10:0x14]])
        # print("%s -> %s" % (src_ip, dst_ip))
        eth = dpkt.ethernet.Ethernet(ip_frame)
        print(eth.type)
        print(dpkt.ethernet.mac_to_str(dest_mac))


        # print('Ethernet Frame: ', dpkt.utils.mac_to_str(eth.src), dpkt.utils.mac_to_str(eth.dst), eth.type)
        # Make sure the Ethernet data contains an IP packet
        if not isinstance(eth.data, dpkt.ip.IP):
            print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)




        # Now access the data within the Ethernet frame (the IP packet)
        # Pulling out src, dst, length, fragment info, TTL, and Protocol
        ip = eth.data
       # print(ip.data)
        #udp = ip.data
        tcp = ip.data
        if isinstance(ip.data, dpkt.tcp.TCP):
            print("TCP")
            print(tcp.data)
            #tcp = ip.data
            #request = dpkt.http.Request(tcp.data)
            #print(repr(request))

        if isinstance(ip.data, dpkt.udp.UDP):
            print("UDP")
        #if isinstance(ip.data, dpkt.arp.ARP):
            #print("ARP")
        #if isinstance(ip.data, dpkt.dns.DNS):
            #print("DNS")
        #if isinstance(ip.data, dpkt.ieee80211.IEEE80211):
            #print("IEEE 802.11")
        #if isinstance(ip.data, dpkt.ethernet.Ethernet):
            #print("ETHERNET")
        # isinstance(ip.data, dpkt.icmp.ICMP):
            #print("ICMP")
        # print("Port:", tcp.dport)
        # print("Ptoto:", ip.get_proto(ip.p))
        # Print out the info, including the fragment flags and offset
        #print('IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d bits=%d)\n' %
           #(dpkt.utils.inet_to_str(ip.src), dpkt.utils.inet_to_str(ip.dst), ip.len, ip.ttl, ip.df, ip.mf, ip.offset))
        # print([dpkt.utils.inet_to_str(ip.src), dpkt.utils.inet_to_str(ip.dst), ip.len, ip.ttl, ip.df, ip.mf, ip.offset])
        # win_pcap.stop()
        print(tcp.sport)
        if tcp.dport == 80:
            http = dpkt.http.Request(tcp.data)
            print(http.data)


        packet = [dpkt.utils.inet_to_str(ip.src), dpkt.utils.inet_to_str(ip.dst), ip.len, ip.ttl, ip.df, ip.mf, ip.offset]

        #db = ScanNetLocalDataBase()

        #db.insertPacket(str(datetime.now()), packet[1], packet[2],"0")

        rowPosition = self.view.ui.tableWidget_2.rowCount()

        self.view.ui.tableWidget_2.insertRow(rowPosition)
        self.view.ui.tableWidget_2.setItem(rowPosition, 0, QTableWidgetItem(str(rowPosition)))
        self.view.ui.tableWidget_2.setItem(rowPosition, 1, QTableWidgetItem(str(packet[0])))
        self.view.ui.tableWidget_2.setItem(rowPosition, 2, QTableWidgetItem(str(packet[1])))
        self.view.ui.tableWidget_2.setItem(rowPosition, 3, QTableWidgetItem(str(packet[2])))
        self.view.ui.tableWidget_2.setItem(rowPosition, 4, QTableWidgetItem(str(packet[3])))
        self.view.ui.tableWidget_2.setItem(rowPosition, 5, QTableWidgetItem(str(packet[4])))
        self.view.ui.tableWidget_2.scrollToBottom()