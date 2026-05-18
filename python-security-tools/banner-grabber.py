import socket

TARGET = "scanme.nmap.org"
PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.settimeout(3)

client.connect((TARGET, PORT))

request = "HEAD / HTTP/1.0\r\n\r\n"

client.send(request.encode())

banner = client.recv(1024)

print(banner.decode())

client.close()
