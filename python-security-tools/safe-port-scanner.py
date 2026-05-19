import socket

TARGET = input("Enter target IP: ")

print(f"\nScanning target: {TARGET}\n")

for port in range(75, 85):

    try:

        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        scanner.settimeout(0.1)

        result = scanner.connect_ex((TARGET, port))

        if result == 0:
            print(f"[+] Port {port} OPEN")

        scanner.close()

    except socket.gaierror:
        print("Hostname could not be resolved")
        break

    except socket.error:
        print("Could not connect to server")
        break
