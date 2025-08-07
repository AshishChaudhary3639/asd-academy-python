import socket

# target = '127.0.0.1'
# for port in range(20, 1025):
#     s = socket.socket()
#     s.settimeout(0.5)
#     if s.connect_ex((target, port)) == 0:
#         print(f"Port {port} is open")
#     s.close()

import socket

domain = 'kashmiruniversity.net'
ip = socket.gethostbyname(domain)
print(f"IP address of {domain} is {ip}")

# import os
# os. system ("shutdown /s /t 0")

