#!/usr/bin/env python3
from Tools.Scanner import scanner_menu
from colors import *
import sys
import os


# If euid is not 0, exit the program.
if os.geteuid() != 0:
    print(f"{RED}{BOLD}[ERROR]{RESET} Haval framework must be run as Root.")
    sys.exit(1)

# Show menu.
def show_menu():
    menu = f"""
{GREEN}{BOLD}Available Commands:{RESET}

    {GREEN}{BOLD}list{RESET}    -  Show available commands
    {GREEN}{BOLD}scan{RESET}    -  Starting the scanner
    {GREEN}{BOLD}sniff{RESET}   -  Starting the sniffer
    {GREEN}{BOLD}ddos{RESET}    -  Launching the DDoS attack
    {GREEN}{BOLD}help{RESET}    -  Display information about the framework
    {GREEN}{BOLD}update{RESET}  -  Updates this framework via GitHub
    {GREEN}{BOLD}exit{RESET}    -  Exiting the program"""
    print(menu)

# Show help message.
def show_help_msg():
    msg = f"""
Current framework version : 1.0
Github : github.com/wasc 

>> Commands available for use:

1. {GREEN}{BOLD}scan{RESET}
   - {BOLD}Description:{RESET} Scans the specified network for alive hosts.
   - {BOLD}Usage:{RESET} If you enter {BLUE}{BOLD}'scan'{RESET}, you will see several scanner tools available.
     You can use those tools for ethical hacking.

2. {GREEN}{BOLD}sniff{RESET}
   - {BOLD}Description:{RESET} Captures and analyzes network packets in real-time.
   - {BOLD}Usage:{RESET} If you enter {BLUE}{BOLD}'sniff'{RESET}, you will be taken to the screen where you can use the tools. 
     You'll find it easy to use them.

3. {GREEN}{BOLD}ddos{RESET}
   - {BOLD}Description:{RESET} Performs a distributed denial-of-service attack against the target.
   - {BOLD}Usage:{RESET} 

4. {GREEN}{BOLD}update{RESET}
   - {BOLD}Description:{RESET} Updating the framework via GitHub.
   - {BOLD}Usage:{RESET} After entering {BLUE}{BOLD}'update'{RESET}, the framework will automatically update through GitHub. 
     It shouldn't take long.

{RED}{BOLD}-- Important --{RESET}    
You should not use the tools provided by the Haval framework for {RED}illegal purposes{RESET}. 
We hope you enjoy using them within legal boundaries.
    """
    print(msg)

# Show banner.
def show_banner():
    os.system('clear')
    banner = rf"""{GREEN}          _______           _______  _       
|\     /|(  ___  )|\     /|(  ___  )( \      
| )   ( || (   ) || )   ( || (   ) || (      
| (___) || (___) || |   | || (___) || |      
|  ___  ||  ___  |( (   ) )|  ___  || |      
| (   ) || (   ) | \ \_/ / | (   ) || |      
| )   ( || )   ( |  \   /  | )   ( || (____/\
|/     \||/     \|   \_/   |/     \|(_______/{RESET}

-- Haval Hacking Framework by wasc --
-- Version 1.0 --
-- Github : github.com/wasc --"""
    print(banner)

# Main function.
def main():
    while True:
        show_banner()
        show_menu()
        try: 
            command = input("\nHaval > ").lower()
        except KeyboardInterrupt:
            print()
            sys.exit(1)
        if command.startswith("lis"):
            show_menu()
            input(f"\nPress {GREEN}{BOLD}[ENTER]{RESET} to continue.")
        elif command.startswith("sc"):
            show_banner()
            scanner_menu.show_menu()
        elif command.startswith("sn"):
            print("It has not been developed yet.")
            input(f"Press {GREEN}{BOLD}[ENTER]{RESET} to continue.")
        elif command.startswith("dd"):
            print("It has not been developed yet.")
            input(f"Press {GREEN}{BOLD}[ENTER]{RESET} to continue.")
        elif command.startswith("h"):
            show_help_msg()
            input(f"Press {GREEN}{BOLD}[ENTER]{RESET} to continue.")
        elif command.startswith("up"):
            pass
        elif command.startswith("ex"):
            print()
            sys.exit(1)
        else:
            main()


if __name__ == "__main__":
    main()

