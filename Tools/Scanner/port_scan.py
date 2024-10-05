from colors import *
import datetime
import socket
import nmap
import time
import os


def show_banner():
    os.system('clear')
    banner = rf"""{GREEN} _______  _______  _______ _________   _______  _______  _______  _       
(  ____ )(  ___  )(  ____ )\__   __/  (  ____ \(  ____ \(  ___  )( (    /|
| (    )|| (   ) || (    )|   ) (     | (    \/| (    \/| (   ) ||  \  ( |
| (____)|| |   | || (____)|   | |     | (_____ | |      | (___) ||   \ | |
|  _____)| |   | ||     __)   | |     (_____  )| |      |  ___  || (\ \) |
| (      | |   | || (\ (      | |           ) || |      | (   ) || | \   |
| )      | (___) || ) \ \__   | |     /\____) || (____/\| )   ( || )  \  |
|/       (_______)|/   \__/   )_(     \_______)(_______/|/     \||/    )_){RESET}
========================================================================="""
    print(banner)

def port_scan(target):
    pscanner = nmap.PortScanner()
    scan_start_time = datetime.datetime.now()
    print(f"\n{BLUE}{BOLD}[*]{RESET} Scan started at {scan_start_time}")
    start_time = time.time()
    try:
        pscanner.scan(hosts=target, ports='1-50000', arguments='-sV -sS -T5')
    except KeyboardInterrupt:
        return
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{BLUE}{BOLD}[*]{RESET} Scanning {target_host} for open ports")
    
    results = []
    for host in pscanner.all_hosts():
        for protocol in pscanner[host].all_protocols():
            ports = pscanner[host][protocol].keys()
            for port in ports:
                service = pscanner[host][protocol][port]['name']
                state = pscanner[host][protocol][port]['state']
                version = pscanner[host][protocol][port].get('version', 'Unknown')
                results.append((port, service, state, version))
    results.sort()

    print(f"{BLUE}{BOLD}[*]{RESET} Scan result for {target_host}({target})\n")
    print(f"{GREEN}{BOLD}PORT     SERVICE       STATUS     VERSION{RESET}")
    for port, service, state, version in results:
        print("{:<8} {:<13} {:<10} {:<8}".format(port, service, state, version))
    print(f"\n{YELLOW}{BOLD}[!]{RESET} Done! scanned in {elapsed_time:.2f} seconds")
    input(f"Press {GREEN}{BOLD}[ENTER]{RESET} to return to the menu.")

def main():
    show_banner()
    global target_host
    try:
        target_host = input("Enter target IP or Domain : ")
    except KeyboardInterrupt:
        return
    target_ip = socket.gethostbyname(target_host)
    port_scan(target_ip)


if __name__ == "__main__":
    main()
