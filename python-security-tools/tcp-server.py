import socket

HOST = "0.0.0.0"
PORT = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(1)

print(f"[+] Listening on port {PORT}...")

client_socket, address = server.accept()

print(f"[+] Connection received from {address}")

data = client_socket.recv(1024)

print(f"[+] Message received: {data.decode()}")

client_socket.close()

server.close()
