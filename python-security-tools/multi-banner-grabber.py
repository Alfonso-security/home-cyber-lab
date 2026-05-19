import socket

TARGET = input("Enter target IP: ")

print(f"\nScanning target: {TARGET}\n")

for port in [21,22,25,80,443,8080]:

    try:

        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        scanner.settimeout(1)

        result = scanner.connect_ex((TARGET, port))

        if result == 0:

            print(f"[+] Port {port} OPEN")

            if port == 80 or port == 8080:

                request = "HEAD / HTTP/1.0\r\n\r\n"

                scanner.send(request.encode())

                banner = scanner.recv(1024)

                print(banner.decode())

        scanner.close()

    except:
        pass
