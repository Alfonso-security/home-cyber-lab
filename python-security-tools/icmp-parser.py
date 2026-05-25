import socket
import struct

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Listening for ICMP packets...\n")

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

        if ip_protocol == 1:

            icmp_header = raw_data[34:38]

            icmph = struct.unpack("!BBH", icmp_header)

            icmp_type = icmph[0]

            code = icmph[1]

            print("\n[ICMP PACKET]")
            print(f"Source IP: {source_ip}")
            print(f"Destination IP: {destination_ip}")
            print(f"ICMP Type: {icmp_type}")
            print(f"Code: {code}")
