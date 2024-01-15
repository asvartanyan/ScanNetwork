import dpkt.ethernet
import dpkt.utils
import psutil
from winpcapy import WinPcapUtils,WinPcapDevices,WinPcap


packet = []
def packet_callback(win_pcap, param, header, pkt_data):
    # Assuming IP (for real parsing use modules like dpkt)
    ip_frame = pkt_data
    # Parse ips
    #print(ip_frame)
    #src_ip = ".".join([str(ord(b)) for b in ip_frame[0xc:0x10]])
    #dst_ip = ".".join([str(ord(b)) for b in ip_frame[0x10:0x14]])
    #print("%s -> %s" % (src_ip, dst_ip))
    eth = dpkt.ethernet.Ethernet(ip_frame)

    print('Ethernet Frame: ', dpkt.utils.mac_to_str(eth.src), dpkt.utils.mac_to_str(eth.dst), eth.type)
    # Make sure the Ethernet data contains an IP packet
    if not isinstance(eth.data, dpkt.ip.IP):
        print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)


    # Now access the data within the Ethernet frame (the IP packet)
    # Pulling out src, dst, length, fragment info, TTL, and Protocol
    ip = eth.data
    tcp = ip.data
    #print("Port:", tcp.dport)
    #print("Ptoto:",ip.get_proto(ip.p))
    # Print out the info, including the fragment flags and offset
    #print('IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' %
          #(dpkt.utils.inet_to_str(ip.src), dpkt.utils.inet_to_str(ip.dst), ip.len, ip.ttl, ip.df, ip.mf, ip.offset))
    packet = [dpkt.utils.inet_to_str(ip.src), dpkt.utils.inet_to_str(ip.dst), ip.len, ip.ttl, ip.df, ip.mf, ip.offset]




    #print(dpkt.ethernet.Ethernet(ip_frame).data)
print(psutil.net_if_addrs())
device = WinPcapDevices.list_devices()
current_device = "Realtek Gaming 2.5GbE Family Controller"
i = 0
for v_dev in WinPcapDevices.list_devices().keys():
    print(v_dev)
    if i == 1:
       current_device = v_dev
    i = i + 1
print(current_device)
WinPcapUtils.capture_on_device_name(current_device, packet_callback)

#WinPcapUtils.capture_on_and_print("*Realtek*")
with WinPcapDevices() as devices:
     for device in devices:
        print (device.name, device.description, device.flags ,device.addresses.contents.netmask.contents.sa_family)

while True:
    print(packet)
