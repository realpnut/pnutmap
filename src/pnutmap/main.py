#!/usr/bin/env python3
import os
import datetime
import subprocess

GREEN = "\033[92m"
RED = "\033[91"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def menu():
    os.system("clear" if os.name != "nt" else "cls")
    print(f"""
         +------------------------+------------------------+
         | 1. Quick Scan          | 6. Stealth Scan        |
         | 2. Full Scan           | 7. Ping Discovery      |
         | 3. Service Detection   | 8. Vulnerability Scan  | 
         | 4. OS Detection        | 9. Trace Route         |      ▄▖    ▗ ▖ ▖    
         | 5. Aggressive Scan     | 10.Firewall Evasion    |      ▙▌▛▌▌▌▜▘▛▖▞▌▀▌▛▌
         +------------------------+------------------------+      ▌ ▌▌▙▌▐▖▌▝ ▌█▌▙▌
         | 11.IPv6 Scan           |                        |              ▌ v0.8.4
         | 12.SSH Brute Force     |                        | 
         | 13. UDP Scan           | 16. Show this menu     | 
         | 14. Top 100 port scan  | 17. Clear              | 
         | 15. Top 1000 port scan | 0. Exit                | 
         +------------------------+------------------------+
    """)

def run_nmap(scan_name, extra_flags):
    target = input(f"{CYAN}Enter target IP or hostname: {RESET}").strip()
    if not target:
        print(f"{RED}Target cannot be empty!{RESET}")
        return

    save = input("Do you want to save the output to a file? (y/N): ").strip().lower()
    cmd = ["nmap"] + extra_flags
    
    if save == 'y':
        filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        cmd += ["-oN", filename]
        print(f"{YELLOW}Performing {scan_name} (Saving to {filename})...{RESET}")
    else:
        print(f"{YELLOW}Performing {scan_name}...{RESET}")
        
    cmd.append(target)
    
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print(f"{RED}Error: 'nmap' is not installed or not in PATH.{RESET}")
    except subprocess.CalledProcessError:
        print(f"{RED}Scan interrupted or failed.{RESET}")

def main():
    menu()
    scan_options = {
        '1':  ("Quick Scan", ["-T4", "-F"]),
        '2':  ("Full Scan", ["-p-", "-T4"]),
        '3':  ("Service Detection", ["-sV"]),
        '4':  ("OS Detection", ["-O"]),
        '5':  ("Aggressive Scan", ["-A"]),
        '6':  ("Stealth Scan", ["-sS"]),
        '7':  ("Ping Discovery", ["-sn"]),
        '8':  ("Vulnerability Scan", ["--script", "vuln"]),
        '9':  ("Trace Route", ["--traceroute"]),
        '10': ("Firewall Evasion Scan", ["-f"]),
        '11': ("IPv6 Scan", ["-6"]),
        '12': ("SSH Brute Force Scan", ["-p", "22", "--script", "ssh-brute"]),
        '13': ("UDP Scan", ["-sU"]),
        '14': ("Top 100 Port Scan", ["--top-ports", "100"]),
        '15': ("Top 1000 Port Scan", ["--top-ports", "1000"]),
    }

    while True:
        opt = input(f"\n{CYAN}Select an option: {RESET}").strip()
        
        if opt in scan_options:
            scan_name, flags = scan_options[opt]
            run_nmap(scan_name, flags)
        elif opt == '16':
            menu()
        elif opt == '17':
            os.system("clear" if os.name != "nt" else "cls")
        elif opt == '0':
            print(f"{GREEN}Exiting...{RESET}")
            break
        else:
            print(f"{RED}Invalid option. Please try again.{RESET}")

if __name__ == "__main__":
    main()
