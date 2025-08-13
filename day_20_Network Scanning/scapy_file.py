from scapy.all import *
import socket
from scapy.layers.inet import ICMP,IP,TCP
import ipaddress
# def ping_host(host):
#     packet=IP(dst=host)/ICMP()
#     reply=sr1(packet,timeout=1,verbose=False)
#     if reply:
#         print(f"{host} is alive")
#     else:
#         print(f"{host} is dead")

# hostname=socket.gethostname()
# local_ip=socket.gethostbyname(hostname)
# print(f"Host name:{hostname}")
# ping_host(local_ip)
network="192.168.29.0/24"
for ip in ipaddress.IPv4Network(network,strict=False):
    packet=IP(dst=str(ip))/ICMP()
    reply=sr1(packet,timeout=1,verbose=False)
    print(f"Checking...... {ip}")
    if reply:
        print(f"{ip} is alive")