#!/usr/bin/env python3
from colors import *
import time
import sys
import os


if os.geteuid() != 0:
    print(f"{RED}[ERROR]{RESET} {BOLD}This script must be run as Root.{RESET}")
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
        choice = str(input(f"{YELLOW}[?]{RESET} {BOLD}Would you like to proceed with the installation? Y/N: {RESET}")).lower()

        if choice.startswith("y"):
            print(f"\n{BLUE}[*]{RESET} {GREEN}Installing required packages ...{RESET}\n")
            time.sleep(0.5)
            try:
                os.system("apt update")
                result = os.system("pip3 install -r requirements.txt --break-system-packages")
            except KeyboardInterrupt:
                print(f"{RED}[-]{RESET} {BOLD}Installation aborted.{RESET}")
                sys.exit(1)
            if result == 0:
                print(f"\n{YELLOW}[!]{RESET} {GREEN}Successfully Installed!\n{RESET}")
            else:
                print(f"\n{RED}[ERROR]{RESET} {BOLD}Installation failed. Please check the error messages and try again.\n{RESET}")
                sys.exit(1)
        elif choice.startswith("n"):
            print(f"\n{RED}[-]{RESET} {BOLD}Installation aborted.\n{RESET}")
            sys.exit(1)
        else:
            input(f"{RED}[-]{RESET} {BOLD}Wrong choice! Press [ENTER] to continue.{RESET}")
            main()
    except KeyboardInterrupt:
        print(f"\n{RED}[-]{RESET} {BOLD}Installation aborted.\n{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()