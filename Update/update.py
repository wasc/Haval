#!/usr/bin/env python3
from colors import *
import subprocess


def main():
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"\n{GREEN}{BOLD}[+]{RESET} Framework updated successfully.")
            print(result.stdout)  
        else:
            print(f"\n{RED}{BOLD}[-]{RESET} Failed to update framework.")
            print(result.stderr)  
    except Exception as e:
        print(f"{RED}{BOLD}[-]{RESET} An error occurred: {e}")

    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
