import socket

TARGET = "8.8.8.8"

hostname = socket.gethostbyaddr(TARGET)

print(hostname)
