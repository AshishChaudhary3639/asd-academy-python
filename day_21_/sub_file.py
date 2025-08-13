import subprocess
target = "192.168.29.232"
# result=subprocess.getoutput(f"nmap {target}")
# print(result)

cmd=f"nmap -A -T4 {target}"
result=subprocess.getoutput(cmd)
print(result)