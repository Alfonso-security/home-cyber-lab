import socket

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Listening for packets...\n")

while True:

    raw_data, addr = sniffer.recvfrom(65535)

    print(raw_data)
