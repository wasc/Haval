#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from colors import *
import time


if os.geteuid() != 0:
    print(f"{RED}{BOLD}[ERROR]{RESET} This script must be run as Root.")
    sys.exit(1)

def main():
    os.system('clear')
    print(r"""
 ═════════════════════════════════════════════════════════════         
              [>>>] Haval Framework Installer [<<<]        
 ══════════════════════════════╦══════════════════════════════   
        [Author]: wasc         ║   [Updated]: 2024|09|27  
 ══════════════════════════════╩══════════════════════════════
""")
    try:
        choice = str(input(f"{YELLOW}{BOLD}[?]{RESET} {BOLD}Would you like to proceed with the installation? Y/N: {RESET}")).lower()

        if choice.startswith("y"):
            print(f"\n{BLUE}[*]{RESET} {GREEN}Installing required packages ...{RESET}\n")
            time.sleep(0.5)
            try:
                os.system("apt update")
                os.system("apt install nmap")
                result = os.system("pip3 install -r requirements.txt --break-system-packages")
            except KeyboardInterrupt:
                print(f"{RED}{BOLD}[-]{RESET} Installation aborted.")
                sys.exit(1)
            if result == 0:
                print(f"\n{YELLOW}[!]{RESET} {GREEN}Successfully Installed!\n{RESET}")
            else:
                print(f"\n{RED}{BOLD}[ERROR]{RESET} Installation failed. Please check the error messages and try again.\n{RESET}")
                sys.exit(1)
        elif choice.startswith("n"):
            print(f"\n{RED}[-]{RESET} {BOLD}Installation aborted.\n{RESET}")
            sys.exit(1)
        else:
            input(f"{RED}[-]{RESET} {BOLD}Wrong choice! Press [ENTER] to continue.{RESET}")
            main()
    except KeyboardInterrupt:
        print(f"\n{RED}{BOLD}[-]{RESET} Installation aborted.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()