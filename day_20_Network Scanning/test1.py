import socket
# Get the hostname of your machine
hostname = socket.gethostname()

# Get the local IP address
local_ip = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"Local IP Address: {local_ip}")

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #IPv4 Addressing,TCP protocol (connection-based).
        # This socket will be used to attempt connecting to the target port.
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) #Return 0 if success
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

target_ip = "192.168.29.232"
# ports_to_scan = [21, 22, 80, 443]
ports_to_scan=[21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080]

print(f"Open ports on {target_ip}: {scan_ports(target_ip, ports_to_scan)}")


##############################################################################
# import socket

# # List of common ports for quick scanning
# common_ports = [21, 22, 23, 25, 53, 80, 110, 143,
#                 443, 445, 3306, 3389, 8080, 5900]

# def scan_ports(target, ports):
#     open_ports = []
#     print(f"\n[*] Scanning {target} ...")
#     for port in ports:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         socket.setdefaulttimeout(1)  # 1 second timeout
#         result = s.connect_ex((target, port))
#         try:
#             service = socket.getservbyport(port, "tcp")
#         except:
#             service="unknown"
#         print(f"[+] Port {port} ({service}) is checked")
#         if result == 0:
#             try:
#                 service = socket.getservbyport(port, "tcp")
#             except:
#                 service = "Unknown"
#             print(f"[+] Port {port} ({service}) is OPEN")
#             open_ports.append((port, service))
#         s.close()
#     return open_ports

# # Target IP (Change to the host you want to test)
# target_ip = "192.168.29.232"

# # Run the scan
# open_ports = scan_ports(target_ip, common_ports)

# print("\nScan complete.")
# if open_ports:
#     print("Open ports found:")
#     for port, service in open_ports:
#         print(f"- {port} ({service})")
# else:
#     print("No open ports found.")



# import socket

# def scan_ports(target, start_port=1, end_port=65535):
#     open_ports = []
#     for port in range(start_port, end_port + 1):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         socket.setdefaulttimeout(0.5)  # shorter timeout for speed
#         result = s.connect_ex((target, port))
#         if result == 0:
#             open_ports.append(port)
#         s.close()
#     return open_ports

# target_ip = "192.168.29.232"
# print(f"Scanning all ports on {target_ip}...")
# open_ports = scan_ports(target_ip)
# print(f"Open ports on {target_ip}: {open_ports}")
