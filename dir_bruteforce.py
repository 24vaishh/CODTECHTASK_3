import requests

def run():
    base_url = input("Enter base URL (e.g., http://example.com/): ")
    wordlist = input("Enter path to directory wordlist: ")

    try:
        with open(wordlist, "r") as f:
            for line in f:
                directory = line.strip()
                url = f"{base_url}{directory}/"
                try:
                    res = requests.get(url, timeout=2)
                    if res.status_code == 200:
                        print(f"[+] Found directory: {url}")
                except:
                    pass
    except FileNotFoundError:
        print("Wordlist file not found.")
