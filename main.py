#!/usr/bin/env python3
import os

def menu():
    print("""
                          ▄▖    ▗ ▖  ▖    
                          ▙▌▛▌▌▌▜▘▛▖▞▌▀▌▛▌
                          ▌ ▌▌▙▌▐▖▌▝ ▌█▌▙▌
                                        ▌ v0.1.0
         +------------------------+------------------------+
         | 1. Quick Scan          | 6. Stealth Scan        |
         | 2. Full Scan           | 7. Ping Discovery      |
         | 3. Service Detection   | 8. Vulnerability Scan  |
         | 4. OS Detection        | 9. Show this menu      |
         | 5. Aggressive Scan     | 0. Exit                |
         +------------------------+------------------------+
      """)

def main():
    menu()
    while True:
        opt = input("Select an option: ")
        if opt == '1':
            target = input("Enter target IP or hostname: ")
            print("Performing Quick Scan...")
            os.system(f"nmap -T4 -F {target}")
        elif opt == '2':
            target = input("Enter target IP or hostname: ")
            print("Performing Full Scan...")
            os.system(f"nmap -p- -T4 {target}")
        elif opt == '3':
            target = input("Enter target IP or hostname: ")
            print("Performing Service Detection...")
            os.system(f"nmap -sV {target}")
        elif opt == '4':
            target = input("Enter target IP or hostname: ")
            print("Performing OS Detection...")
            os.system(f"nmap -O {target}")
        elif opt == '5':
            target = input("Enter target IP or hostname: ")
            print("Performing Aggressive Scan...")
            os.system(f"nmap -A {target}")
        elif opt == '6':
            target = input("Enter target IP or hostname: ")
            print("Performing Stealth Scan...")
            os.system(f"nmap -sS {target}")
        elif opt == '7':
            target = input("Enter target IP or hostname: ")
            print("Performing Ping Discovery...")
            os.system(f"nmap -sn {target}")
        elif opt == '8':
            target = input("Enter target IP or hostname: ")
            print("Performing Vulnerability Scan...")
            os.system(f"nmap --script vuln {target}")
        elif opt == '9':
            menu()
        elif opt == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
