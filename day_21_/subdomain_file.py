import requests

def find_subdomains(domain, wordlist):
    found_subdomains = []

    for word in wordlist:
        subdomain = f"{word}.{domain}"
        url = f"http://{subdomain}"
        try:
            response = requests.get(url, timeout=3)
            print(f"[+] Found: {subdomain}")
            found_subdomains.append(subdomain)
        except requests.ConnectionError:
            pass  # Subdomain does not exist

    return found_subdomains

if __name__ == "__main__":
    target_domain = "example.com"  # Change this to your target
    # Small example wordlist
    subdomain_list = ["www", "mail", "ftp", "test", "dev,beta"]

    print(f"[*] Starting subdomain enumeration for {target_domain}...")
    found = find_subdomains(target_domain, subdomain_list)

    print("\n=== Found Subdomains ===")
    for sub in found:
        print(sub)
