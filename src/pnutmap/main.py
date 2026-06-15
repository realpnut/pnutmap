#!/usr/bin/env python3
import os
import datetime
import shutil
import sys

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def menu():
    os.system("clear")
    print("""
                                      ▄▖    ▗ ▖  ▖    
                                      ▙▌▛▌▌▌▜▘▛▖▞▌▀▌▛▌
                                      ▌ ▌▌▙▌▐▖▌▝ ▌█▌▙▌
                                                   ▌ v0.8.1
         +------------------------+------------------------+------------------------+
         | 1. Quick Scan          | 6. Stealth Scan        | 11.IPv6 Scan           |
         | 2. Full Scan           | 7. Ping Discovery      | 12.SSH Brute Force     |
         | 3. Service Detection   | 8. Vulnerability Scan  | 13. UDP Scan           |
         | 4. OS Detection        | 9. Trace Route         | 14. Show this Menu     |
         | 5. Aggressive Scan     | 10.Firewall Evasion    | 0. Exit                |
         +------------------------+------------------------+------------------------+
      """
)
menu()
while True:
    opt = input(f"{CYAN}Select an option: {RESET}")
    if opt == '1':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing Quick Scan...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap -T4 -F {target} | tee {filename}")
        else:
            os.system(f"nmap -T4 -F {target}")
    elif opt == '2':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing Full Scan...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap -p- -T4 {target} | tee {filename}")
        else:
            os.system(f"nmap -p- -T4 {target}")
    elif opt == '3':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing Service Detection...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap -sV {target} | tee {filename}")
        else:
            os.system(f"nmap -sV {target}")
    elif opt == '4':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing OS Detection...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap -O {target} | tee {filename}")
        else:
            os.system(f"nmap -O {target}")
    elif opt == '5':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing Aggressive Scan...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap -A {target} | tee {filename}")
        else:
            os.system(f"nmap -A {target}")
    elif opt == '6':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing Stealth Scan...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap -sS {target} | tee {filename}")
        else:
            os.system(f"nmap -sS {target}")
    elif opt == '7':
        target = input("Enter target IP or hostname: ")
        print(f"{YELLOW}Performing Ping Discovery...{RESET}")
        os.system(f"nmap -sn {target}")
    elif opt == '8':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing Vulnerability Scan...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap --script vuln {target} | tee {filename}")
        else:
            os.system(f"nmap --script vuln {target}")
    elif opt == '9':
        target = input("Enter target IP or hostname: ")
        print(f"{YELLOW}Performing Trace Route...{RESET}")
        os.system(f"nmap --traceroute {target}")
    elif opt == '10':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing Firewall Evasion Scan...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap -f {target} | tee {filename}")
        else:
            os.system(f"nmap -f {target}")
    elif opt == '11':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing IPv6 Scan...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap -6 {target} | tee {filename}")
        else:
            os.system(f"nmap -6 {target}")

    elif opt == '12':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing SSH Brute Force Scan...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap -p 22 --script ssh-brute {target} | tee {filename}")
        else:
            os.system(f"nmap -p 22 --script ssh-brute {target}")

    elif opt == '13':
        target = input("Enter target IP or hostname: ")
        save = input("Do you want to save the output to a file? (y/N): ")
        print(f"{YELLOW}Performing UDP Scan...{RESET}")
        if save.lower() == 'y':
            filename = f"pnutmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            os.system(f"nmap -sU {target} | tee {filename}")
        else:
            os.system(f"nmap -sU {target}")
    
    elif opt == '14':
        menu()

    elif opt == '0':
        print(f"{GREEN}Exiting...{RESET}")
        break
    else:
        print(f"{RED}Invalid option. Please try again.{RESET}")
