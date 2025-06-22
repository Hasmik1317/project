import requests

target_url = input("[*] Enter Target URL (e.g., http://example.com/): ")
file_name = input("[*] Enter name of the file containing directories: ")

def request_url(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        return None

try:
    with open(file_name, 'r') as file:
        for line in file:
            directory = line.strip()
            full_url = target_url.rstrip('/') + '/' + directory
            response = request_url(full_url)
            if response and response.status_code == 200:
                print(f"[+] Discovered Directory at this path: {full_url}")
except FileNotFoundError:
    print(f"[-] File '{file_name}' not found.")
