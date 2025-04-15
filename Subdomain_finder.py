import requests

def run():
    domain = input("Enter domain (e.g., example.com): ")
    wordlist = input("Enter path to subdomain wordlist: ")

    try:
        with open(wordlist, "r") as f:
            for sub in f:
                sub = sub.strip()
                url = f"http://{sub}.{domain}"
                try:
                    res = requests.get(url, timeout=2)
                    print(f"[+] Found: {url}")
                except:
                    pass
    except FileNotFoundError:
        print("Wordlist file not found.")
