from scapy.all import *
from scapy.layers.inet import ICMP, IP,TCP
from scapy.layers.l2 import ARP, Ether

# def ping_host(host):
#     packet = IP(dst=host)/ICMP()   #Creates an IP layer in the packet.,
#     reply = sr1(packet, timeout=1, verbose=False)
#     if reply:
#         print(f"{host} is alive")
#     else:
#         print(f"{host} is down")

# ping_host("192.168.29.232")

# from scapy.all import ICMP, IP, sr1
# import ipaddress

# # Define network range
# network = "192.168.29.0/24"  # Change to your network range

# # Generate all IPs in the range (excluding network/broadcast addresses)
# for ip in ipaddress.IPv4Network(network, strict=False):
#     # Create ICMP ping packet
#     packet = IP(dst=str(ip)) / ICMP()

#     # Send packet and wait for reply
#     reply = sr1(packet, timeout=1, verbose=False)

#     if reply:
#         print(f"{ip} is alive")



# Step 1: Discover live hosts with ARP scan
def discover_hosts(network):
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=False)[0]

    hosts = []
    for sent, received in result:
        hosts.append({'ip': received.psrc, 'mac': received.hwsrc})
    return hosts

# Step 2: Scan open ports on a host (TCP SYN scan)
def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        pkt = IP(dst=ip) / TCP(dport=port, flags="S")  # SYN packet
        resp = sr1(pkt, timeout=1, verbose=False)
        if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:  # SYN+ACK
            open_ports.append(port)
            # Send RST to close connection
            sr1(IP(dst=ip)/TCP(dport=port, flags="R"), timeout=1, verbose=False)
    return open_ports

# Step 3: Main execution
network_range = "192.168.29.0/24"  # Change to your network range
ports_to_scan = [22, 80, 443]  # Common ports: SSH, HTTP, HTTPS

print("[*] Scanning network for live hosts...")
live_hosts = discover_hosts(network_range)

if not live_hosts:
    print("No live hosts found.")
else:
    print("\nLive hosts found:")
    print("IP Address\t\tMAC Address\t\tOpen Ports")
    print("-----------------------------------------------------------")
    for host in live_hosts:
        open_ports = scan_ports(host['ip'], ports_to_scan)
        print(f"{host['ip']}\t{host['mac']}\t{open_ports}")
