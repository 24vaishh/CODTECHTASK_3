import hashlib

def run():
    hash_input = input("Enter hash to crack: ")
    wordlist = input("Enter path to wordlist: ")

    try:
        with open(wordlist, "r") as f:
            for word in f:
                word = word.strip()
                if hashlib.sha256(word.encode()).hexdigest() == hash_input:
                    print(f"[+] Password found: {word}")
                    return
        print("[-] Password not found in wordlist.")
    except FileNotFoundError:
        print("Wordlist file not found.")
