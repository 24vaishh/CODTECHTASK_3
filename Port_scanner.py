import socket

def run():
    target = input("Enter target IP: ")
    ports = [21, 22, 23, 80, 443, 3306, 8080]

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()
