import random

import getmac
import psutil
import requests
import json
import folium
import scapy.utils
from winpcapy import WinPcapUtils,WinPcapDevices,WinPcap
import dpkt.ethernet
import dpkt.utils
from threading import Thread
from getmac import get_mac_address
from scapy import interfaces
class Model:
    endpoints_nets = None
    interfaces = []
    current_interface_index = -1
    current_interface_name = ""
    current_interface_MAC = ""
    current_interface_f_name = ""
    packets = []
    packet_capture_thread = Thread()

    def __init__(self,num=0):
        self.num = num
        #self.packet_capture_thread = Thread(target=start_capture,args=(self.current_interface_name,))


        ips = ["173.194.222.100","93.186.255.194"]

        #print(ans)

    def increment(self):
        self.num += 1

    def getNetConnectionList(self):

        net_conn_list = []
        ips_list = []
        ps = psutil.net_connections(kind="all")
        nets = []
        for p in ps:
            if len(p.raddr) == 2:
                net = {'ip': str(p.raddr.ip), 'port': str(p.raddr.port), 'country': "", 'city': "",'lat': 0, 'lon': 0}
                net_conn_list.append(net)
                ips_list.append(str(p.raddr.ip))
        #try:
        if True:
          url = 'http://ip-api.com/batch'
          response = requests.post(url, data=json.dumps(ips_list)).json()

          #ans = response[1].get("country")
          for ans in response:
              ip = str(ans.get("query"))
              country = str(ans.get("country"))
              city = str(ans.get("city"))
              lat = ans.get("lat")
              lon = ans.get("lon")
              for net in net_conn_list:
                  if ip == net["ip"]:
                      net["country"] = country
                      net["city"] = city
                      net["lat"] = lat
                      net["lon"] = lon

        #except:
        else:
            print("Ошибка при получении Endpoints List")

        self.endpoints_nets = net_conn_list
        return net_conn_list

    def getFoliumMapWithMarkers(self,net_conn_list):
        _map = folium.Map()
        nets = net_conn_list
        rnd = (random.random()/10000)
        for net in nets:
            lat = net["lat"]
            lon = net["lon"]
            if ((lat != None) and (lon != None)):
                coord = [lat+rnd,lon+rnd]
                folium.Marker(location=coord).add_to(_map)
        return _map

    def getListInterfaces(self):
        self.interfaces = WinPcapDevices.list_devices()
        return self.interfaces

    def updateNameCurrentInterface(self):
        i = 0


        for (v_dev,key) in zip(WinPcapDevices.list_devices().keys(),WinPcapDevices.list_devices().values()):
            if self.current_interface_index == i:
                self.current_interface_name = v_dev
                self.current_interface_f_name = key
                break

            i = i + 1

    def startCapture(self):
        print(self.current_interface_name)
        #self.packet_capture_thread.start()




    def stopCapture(self):
        #self.packet_capture_thread.join()
        pass

def start_capture(current_interface_name):
    WinPcapUtils.capture_on_device_name(current_interface_name, packet_callback)

def packet_callback(win_pcap, param, header, pkt_data):
    # Assuming IP (for real parsing use modules like dpkt)
    ip_frame = pkt_data
    # Parse ips
    # print(ip_frame)
    # src_ip = ".".join([str(ord(b)) for b in ip_frame[0xc:0x10]])
    # dst_ip = ".".join([str(ord(b)) for b in ip_frame[0x10:0x14]])
    # print("%s -> %s" % (src_ip, dst_ip))
    eth = dpkt.ethernet.Ethernet(ip_frame)

    print('Ethernet Frame: ', dpkt.utils.mac_to_str(eth.src), dpkt.utils.mac_to_str(eth.dst), eth.type)
    # Make sure the Ethernet data contains an IP packet
    if not isinstance(eth.data, dpkt.ip.IP):
       print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)

    # Now access the data within the Ethernet frame (the IP packet)
    # Pulling out src, dst, length, fragment info, TTL, and Protocol
    ip = eth.data
    tcp = ip.data
    print("Port:", tcp.dport)
    print("Ptoto:", ip.get_proto(ip.p))
    # Print out the info, including the fragment flags and offset
    print('IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' %
       (dpkt.utils.inet_to_str(ip.src), dpkt.utils.inet_to_str(ip.dst), ip.len, ip.ttl, ip.df, ip.mf, ip.offset))
    #print([dpkt.utils.inet_to_str(ip.src), dpkt.utils.inet_to_str(ip.dst), ip.len, ip.ttl, ip.df, ip.mf, ip.offset])





