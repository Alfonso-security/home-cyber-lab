import socket

TARGET = input("Enter target IP: ")

print(f"\nScanning target: {TARGET}\n")

VULNERABLE_BANNERS = [
    "OpenSSH_6",
    "Apache/2.2",
    "vsFTPd 2.3.4"
]

for port in [21,22,80,8080]:

    try:

        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        scanner.settimeout(2)

        result = scanner.connect_ex((TARGET, port))

        if result == 0:

            print(f"[+] Port {port} OPEN")

            if port == 80 or port == 8080:

                request = "HEAD / HTTP/1.0\r\n\r\n"

                scanner.send(request.encode())

            banner = scanner.recv(1024).decode(errors="ignore")

            print(f"[BANNER] {banner}")

            for vuln in VULNERABLE_BANNERS:

                if vuln in banner:

                    print(f"[!] Possible vulnerable service detected: {vuln}")

        scanner.close()

    except:
        pass
