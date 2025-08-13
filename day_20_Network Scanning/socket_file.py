import socket
hostname=socket.gethostname()
local_ip=socket.gethostbyname(hostname)
print(f"Host name:{hostname}")
print(f"Local IP address:{local_ip}")

def scan_ports(target,ports):
    open_ports=[]
    for port in ports:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
        try:
            service=socket.getservbyport(port,"tcp")
        except Exception as e:
            print(e)
            service="Unknown"
        print(f"Port {port} {service} is checked")
        if result==0:
            open_ports.append(port)
        s.close()
    return open_ports
target_ip=local_ip
ports_to_scan=[21,22,23,25,53,80,110,143,443,445,3306,3389,8080,5900]
print(f"Open ports on {target_ip}:{scan_ports(target_ip,ports_to_scan)}")