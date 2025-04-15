from modules import port_scanner, brute_forcer, subdomain_finder, dir_bruteforce, hash_cracker

def main():
    while True:
        print("\n--- Penetration Testing Toolkit ---")
        print("1. Port Scanner")
        print("2. HTTP Brute Forcer")
        print("3. Subdomain Finder")
        print("4. Directory Brute-Forcer")
        print("5. Hash Cracker")
        print("6. Exit")

        choice = input("Select a tool: ")

        if choice == '1':
            port_scanner.run()
        elif choice == '2':
            brute_forcer.run()
        elif choice == '3':
            subdomain_finder.run()
        elif choice == '4':
            dir_bruteforce.run()
        elif choice == '5':
            hash_cracker.run()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
