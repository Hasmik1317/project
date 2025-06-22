import scapy.all as scapy
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP Address or Range')
    options = parser.parse_args()

    if not options.target:
        parser.error("[-] Please specify an IP address or range, use --help for more info.")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    result = []
    for sent, received in answered_list:
        client = {"ip": received.psrc, "mac": received.hwsrc}
        result.append(client)
    return result

def display_result(result):
    print("\nIP Address\t\tMAC Address")
    print("-" * 40)
    for client in result:
        print(f"{client['ip']}\t\t{client['mac']}")

options = get_args()
scanned_output = scan(options.target)
display_result(scanned_output)
