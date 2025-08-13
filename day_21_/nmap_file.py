import nmap
import json
import os
# os.system("nmap --version")

# Initialize scanner
nm = nmap.PortScanner()

# Target (change as needed)
target = "192.168.29.232"

# Function to pretty print results
def print_results(results):
    print(json.dumps(results, indent=4))


def print_results_basic(results, filename="results.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
    print(f"[+] Results saved to {filename}")



def print_specific_ports(results, ports):
    if target in results["scan"]:
        host_info = results["scan"][target]
        if "tcp" in host_info:
            found = False
            for port in ports:
                if port in host_info["tcp"]:
                    details = host_info["tcp"][port]
                    print(f"{port}/tcp {details['state']} {details['name']}")
                    found = True
            if not found:
                print("No specified ports found open or detected.")
        else:
            print("No TCP ports detected.")
    else:
        print("No results found for target.")


def print_service_versions(results):
    if target in results["scan"]:
        host_info = results["scan"][target]
        if "tcp" in host_info:
            for port, details in host_info["tcp"].items():
                product = details.get("product", "")
                version = details.get("version", "")
                extrainfo = details.get("extrainfo", "")
                print(f"{port}/tcp {details['state']} {details['name']} {product} {version} {extrainfo}".strip())
        else:
            print("No TCP ports detected.")
    else:
        print("No results found for target.")


def print_os_info(results):
    if target in results["scan"]:
        host_info = results["scan"][target]
        if "osmatch" in host_info:
            print("\n--- OS Detection Results ---")
            for os in host_info["osmatch"]:
                name = os.get("name", "Unknown OS")
                accuracy = os.get("accuracy", "0")
                print(f"OS Guess: {name} (Accuracy: {accuracy}%)")
        else:
            print("No OS detection data found.")
    else:
        print("No results found for target.")


# 1. Basic Scan
# print("\n[1] Basic Scan")
# print_results(nm.scan(target))
# print_results_basic(nm.scan(target))

# 2. Multiple IPs
# print("\n[2] Multiple IPs Scan")
# print_results(nm.scan("scanme.nmap.org scanme2.nmap.org"))

# nm.scan(hosts='192.168.29.1-3',arguments='-sP')
# for host in nm.all_hosts():
#     print(f"{host} :{nm[host].state()}")


# # 3. Specific Ports
print("\n[3] Specific Ports (80,443)")
# print_results(nm.scan(target, "21,139,80,443,445,5432"))

# results = nm.scan(target, "21,139,80,443,445,5432")
# print_specific_ports(results, [21,139, 80, 443,445,5432])


# nm.scan(target, "21,80,443")
# print(nm[target].state())
# print(nm[target]['tcp'][443]['state'])



# # 4. All Ports
# print("\n[4] All Ports (1-65535)")
# print_results(nm.scan(target, "1-65535"))

# 5. Service Version Detection
# print("\n[5] Service Version Detection (-sV)")
# print_results(nm.scan(target, arguments="-sV"))

# Run service version detection (-sV)
# scan_results = nm.scan(target, arguments="-sV")
# print_service_versions(scan_results)

# 6. OS Detection
# print("\n[6] OS Detection (-O)")
# # # print_results(nm.scan(target, arguments="-O"))
# scan_results = nm.scan(target, arguments="-O")
# print_os_info(scan_results)

# nm.scan(target, arguments="-O")
# print(nm[target]['osmatch'][0])

# 7. Aggressive Scan
print("\n[7] Aggressive Scan (-A)")
print_results(nm.scan(target, arguments="-A"))

# # 8. SYN Scan
# print("\n[8] SYN Scan (-sS)")
# print_results(nm.scan(target, arguments="-sS"))

# # 9. UDP Scan
# print("\n[9] UDP Scan (-sU)")
# print_results(nm.scan(target, arguments="-sU"))

# 10. Ping Scan (Host Discovery)
# print("\n[10] Ping Scan (-sn)")
# print_results(nm.scan(target, arguments="-sn"))

# # 11. Script Scan (vulnerability check)
# print("\n[11] Script Scan (--script=vuln)")
# print_results(nm.scan(target, arguments="--script=vuln"))

# # 12. Custom Advanced Scan
# print("\n[12] Advanced Scan (-sS -sV -O -p 1-1000 -T4)")
# print_results(nm.scan(target, "1-1000", arguments="-sS -sV -O -T4"))
