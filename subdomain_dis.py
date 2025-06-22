import requests

domain = "target.com"
with open("subdomains.txt") as f:
    subdomains = f.read().splitlines()

discovered = []
for sub in subdomains:
    url = f"http://{sub}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain:", url)
        discovered.append(url)

with open("discovered_subdomains.txt", "w") as out:
    for url in discovered:
        out.write(url + "\n")
