from colors import *
import netifaces
import tabulate
import nmap
import time
import os


def show_banner():
    os.system('clear')
    banner = rf"""{GREEN} _        _______ _________          _______  _______  _          _______  _______  _______  _       
( (    /|(  ____ \\__   __/|\     /|(  ___  )(  ____ )| \    /\  (  ____ \(  ____ \(  ___  )( (    /|
|  \  ( || (    \/   ) (   | )   ( || (   ) || (    )||  \  / /  | (    \/| (    \/| (   ) ||  \  ( |
|   \ | || (__       | |   | | _ | || |   | || (____)||  (_/ /   | (_____ | |      | (___) ||   \ | |
| (\ \) ||  __)      | |   | |( )| || |   | ||     __)|   _ (    (_____  )| |      |  ___  || (\ \) |
| | \   || (         | |   | || || || |   | || (\ (   |  ( \ \         ) || |      | (   ) || | \   |
| )  \  || (____/\   | |   | () () || (___) || ) \ \__|  /  \ \  /\____) || (____/\| )   ( || )  \  |
|/    )_)(_______/   )_(   (_______)(_______)|/   \__/|_/    \/  \_______)(_______/|/     \||/    )_){RESET}
===================================================================================================="""
    print(banner)

def get_interface():
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        if iface == "lo":
            continue
        current_iface = iface
    return current_iface   

def get_local_ip():
    interface = get_interface()
    ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]["addr"]
    return ipv4

def show_network_details():
    interface = get_interface()
    local_ip = get_local_ip()
    gateway_ip = netifaces.gateways()["default"][netifaces.AF_INET][0]
    print(f"Current interface   :   {BLUE}{BOLD}{interface}{RESET}")
    print(f"Local IP Address    :   {BLUE}{BOLD}{local_ip}{RESET}")
    print(f"Gateway IP Adress   :   {BLUE}{BOLD}{gateway_ip}{RESET}")

def show_menu():
    menu = f"""
{GREEN}{BOLD}Available Options:{RESET}

    {GREEN}{BOLD}1{RESET}) Scan alive hosts on your network
    {GREEN}{BOLD}2{RESET}) Coming Soon

Type {GREEN}{BOLD}'Back'{RESET} or {GREEN}{BOLD}'Ctrl + C'{RESET} to return to the menu.
    """
    print(menu)

def alive_hosts_scan():
    local_ip = get_local_ip()
    ip_range = '.'.join(local_ip.split('.')[:-1] + ['0'])
    scan_range = f'{ip_range}/24'

    print(f"\n{BLUE}{BOLD}[*]{RESET} Scanning hosts from 192.168.45.1 to 192.168.45.254 ({scan_range})")

    nm = nmap.PortScanner()
    start_time = time.time()
    try:
        nm.scan(hosts=scan_range, arguments='-O -sS -T5')
    except KeyboardInterrupt:
        return
    end_time = time.time()
    elapsed_time = end_time - start_time

    alive_hosts = []
    for host in nm.all_hosts():
        if nm[host].state() == "up":
            hostname = nm[host].hostname()
            mac_address = nm[host]['addresses'].get('mac', 'Unknown MAC')
            os_info = nm[host].get('osclass', [])
            os_info_str = ', '.join(os_class['osfamily'] for os_class in os_info)
            
            local_ip = get_local_ip()
            if host == local_ip:
                hostname = hostname + f"{GREEN}{BOLD}(This Device){RESET}"

            if hostname.startswith("_"):
                hostname = hostname[1:]
            host_info = {
                "IP Address": host,
                "Host Name": hostname,
                "MAC Adresss": mac_address,
                "OS Information": os_info_str if os_info_str else 'Unknown OS',
                "Status": "Alive"
            }
            alive_hosts.append(host_info)

    if alive_hosts:
        print(f"\n[{GREEN}{BOLD}+{RESET}] {GREEN}{BOLD}Alive Hosts Found:{RESET}")
        print(tabulate.tabulate(alive_hosts, headers="keys", tablefmt="fancy_grid"))
        print(f"\n{YELLOW}{BOLD}[!]{RESET} Done! scanned in {elapsed_time:.2f} seconds")
        input(f"Press {GREEN}{BOLD}[ENTER]{RESET} to return to the menu.")
    else:
        print(f"{RED}{BOLD}[-]{RESET} No alive hosts found.")
        input(f"\nPress {GREEN}{BOLD}[ENTER]{RESET} to return to the menu.")

def main():
    while True:
        show_banner()
        show_network_details()
        show_menu()
        try:
            choice = input("Haval/Scan > ").lower()
        except KeyboardInterrupt:
            return
        
        if choice == "1":
            alive_hosts_scan()
        elif choice.startswith("bac") or choice.startswith("qui"):
            return
        else:
            continue

    
if __name__ == "__main__":
    main()


    