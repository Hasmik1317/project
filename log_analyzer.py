import re

def analyze_log(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        if re.search(r'Failed login', line, re.IGNORECASE):
            print(f"[!] Suspicious: {line.strip()}")

if __name__ == "__main__":
    path = input("Enter path to log file (e.g., /var/log/auth.log): ").strip()
    analyze_log(path)
