import re

def identify_hash(h):
    if re.fullmatch(r"[a-fA-F0-9]{32}", h):
        return "MD5"
    elif re.fullmatch(r"[a-fA-F0-9]{40}", h):
        return "SHA1"
    elif re.fullmatch(r"[a-fA-F0-9]{64}", h):
        return "SHA256"
    else:
        return "Unknown"

if __name__ == "__main__":
    h = input("Enter hash: ").strip()
    print("Hash type:", identify_hash(h))
