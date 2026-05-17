import socket

TARGET = "127.0.0.1"
PORTS = [22, 80, 443, 7777, 8080]

for port in PORTS:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((TARGET, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is CLOSED")

    scanner.close()
