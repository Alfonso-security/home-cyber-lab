import socket

TARGET = "127.0.0.1"

print(f"Scanning target: {TARGET}")

for port in range(1, 1025):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(0.5)

    result = scanner.connect_ex((TARGET, port))

    if result == 0:
        print(f"[+] Port {port} OPEN")

    scanner.close()
