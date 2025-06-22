import hashlib
import os

def detect_hash_type(hash_str):
    length = len(hash_str)
    if length == 32:
        return "md5"
    elif length == 64:
        return "sha256"
    else:
        return None

def crack_hash_auto(target_hash, wordlist_path):
    hash_type = detect_hash_type(target_hash)

    if not hash_type:
        print("Unsupported or unknown hash type.")
        return

    print(f"Hash type detected: {hash_type}")
    print(f"Using wordlist: {wordlist_path}")

    if not os.path.exists(wordlist_path):
        print("Wordlist not found.")
        return

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
        for word in file:
            word = word.strip()

            if hash_type == "md5":
                hashed = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "sha256":
                hashed = hashlib.sha256(word.encode()).hexdigest()

            if hashed == target_hash:
                print(f"Password found: {word}")
                return

            print(f"Tried: {word}")

    print("Password not found.")

target_hash = input("Enter hash: ").strip()
wordlist_path = "wordlist.txt"

crack_hash_auto(target_hash, wordlist_path)
