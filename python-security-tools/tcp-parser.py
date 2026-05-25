import socket
import struct

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Listening for TCP packets...\n")

while True:

    raw_data, addr = sniffer.recvfrom(65535)

    ethernet_header = raw_data[0:14]

    eth = struct.unpack("!6s6sH", ethernet_header)

    protocol = socket.htons(eth[2])

    if protocol == 8:

        ip_header = raw_data[14:34]

        iph = struct.unpack("!BBHHHBBH4s4s", ip_header)

        source_ip = socket.inet_ntoa(iph[8])

        destination_ip = socket.inet_ntoa(iph[9])

        ip_protocol = iph[6]

        if ip_protocol == 6:

            tcp_header = raw_data[34:54]

            tcph = struct.unpack("!HHLLBBHHH", tcp_header)

            source_port = tcph[0]

            destination_port = tcph[1]

            flags = tcph[5]

            print("\n[TCP PACKET]")
            print(f"Source IP: {source_ip}:{source_port}")
            print(f"Destination IP: {destination_ip}:{destination_port}")
            print(f"Flags: {flags}")
