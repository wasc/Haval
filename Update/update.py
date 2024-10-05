#!/usr/bin/env python3
from colors import *
import subprocess
import time
import sys


def loading():
    chars = ['/', '-', '\\', '|']
    for _ in range(6):  
        for char in chars:
            sys.stdout.write('\r' + f"{BLUE}{BOLD}[*]{RESET} Updating the framework ...{char}")  
            sys.stdout.flush()  
            time.sleep(0.1)

def main():
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        if result.returncode == 0:
            time.sleep(0.3)
            loading()
            print(f"{GREEN}{BOLD}[+]{RESET} Framework updated successfully!")
            print(f"\nPlease restart the program. {GREEN}{BOLD}\"sudo python Haval.py\"{RESET}")
            sys.exit(1)
        else:
            time.sleep(0.3)
            loading()
            print("\n", result.stderr)  
            print(f"\n{RED}{BOLD}[-]{RESET} Failed to update framework.")
            input(f"Press {GREEN}{BOLD}[ENTER]{RESET} to continue.")
    except Exception as e:
        print(f"{RED}{BOLD}[-]{RESET} An error occurred: {e}")
        input(f"Press {GREEN}{BOLD}[ENTER]{RESET} to continue.")

    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
