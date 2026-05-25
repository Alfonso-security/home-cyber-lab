# 🌐 Python UDP Packet Parser

This project demonstrates how to capture and analyze UDP packets using Python raw sockets.

The script extracts:
- source IP
- destination IP
- source port
- destination port
- UDP packet length

This lab focuses on real UDP/DNS traffic analysis.

---

# 📌 Objective

Understand:
- UDP packet parsing
- DNS traffic analysis
- raw socket capture
- source and destination ports
- connectionless communication
- packet length
- network traffic monitoring

---

# 📂 File

| File | Description |
|---|---|
| `udp-parser.py` | UDP packet parser and analyzer |

---

# 🐍 Python Code

```python
import socket
import struct

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Listening for UDP packets...\n")

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

        if ip_protocol == 17:

            udp_header = raw_data[34:42]

            udph = struct.unpack("!HHHH", udp_header)

            source_port = udph[0]

            destination_port = udph[1]

            length = udph[2]

            print("\n[UDP PACKET]")
            print(f"Source IP: {source_ip}:{source_port}")
            print(f"Destination IP: {destination_ip}:{destination_port}")
            print(f"Length: {length}")
```

---

# 📌 Code Explanation

## Import libraries

```python
import socket
import struct
```

| Module | Purpose |
|---|---|
| `socket` | networking |
| `struct` | binary packet parsing |

Mental model:

```text
socket = network communication endpoint
struct = binary packet interpreter
```

---

## Raw socket creation

```python
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
```

Creates a raw packet sniffer.

Mental model:

```text
listen directly to network packets
```

---

## Ethernet header extraction

```python
ethernet_header = raw_data[0:14]
```

Extracts the first 14 bytes of the Ethernet frame.

The Ethernet header contains:
- destination MAC
- source MAC
- protocol type

---

## Ethernet unpacking

```python
eth = struct.unpack("!6s6sH", ethernet_header)
```

Interprets the Ethernet header fields.

Mental translation:

```text
unpack = open structured binary data
```

---

## IPv4 detection

```python
if protocol == 8:
```

Checks if the Ethernet frame contains IPv4 traffic.

---

## IP header extraction

```python
ip_header = raw_data[14:34]
```

Extracts the IPv4 header.

---

## IP unpacking

```python
iph = struct.unpack("!BBHHHBBH4s4s", ip_header)
```

Interprets IPv4 header fields.

The IP header contains:
- source IP
- destination IP
- protocol number
- TTL

---

## Source and destination IP

```python
source_ip = socket.inet_ntoa(iph[8])
destination_ip = socket.inet_ntoa(iph[9])
```

Converts binary IP addresses into readable IP addresses.

Mental translation:

```text
inet_ntoa = binary IP to readable IP
```

---

## IP protocol detection

```python
ip_protocol = iph[6]
```

Extracts the protocol used inside the IP packet.

| Value | Protocol |
|---|---|
| `1` | ICMP |
| `6` | TCP |
| `17` | UDP |

---

## UDP detection

```python
if ip_protocol == 17:
```

Checks if the packet contains UDP traffic.

---

## UDP header extraction

```python
udp_header = raw_data[34:42]
```

Extracts the UDP header.

A UDP header is 8 bytes long.

---

## UDP unpacking

```python
udph = struct.unpack("!HHHH", udp_header)
```

Interprets UDP header fields.

| Field | Meaning |
|---|---|
| source port | sender service port |
| destination port | receiver service port |
| length | UDP packet size |
| checksum | error-checking value |

---

## Source and destination ports

```python
source_port = udph[0]
destination_port = udph[1]
```

Extracts UDP ports.

Mental model:

```text
IP = device
port = service
```

---

## UDP length

```python
length = udph[2]
```

Shows UDP packet size.

---

# 🚀 Practical Test

## Run parser

```bash
sudo python3 udp-parser.py
```

---

## Generate DNS Traffic

Open another terminal:

```bash
nslookup google.com
```

or:

```bash
dig google.com
```

---

# 📌 Example Output

```text
[UDP PACKET]
Source IP: 10.0.2.15:34587
Destination IP: 192.168.1.1:53
Length: 59

[UDP PACKET]
Source IP: 192.168.1.1:53
Destination IP: 10.0.2.15:34587
Length: 91
```

---

# 📌 DNS Traffic Analysis

Port `53` is commonly used by DNS.

Example:

```text
10.0.2.15 → 192.168.1.1:53
```

This represents a DNS request.

```text
192.168.1.1:53 → 10.0.2.15
```

This represents a DNS response.

---

# 🧠 TCP vs UDP Mental Model

```text
TCP = phone call
UDP = send a message without waiting for confirmation
```

TCP uses:
- handshake
- ACK
- connection state

UDP uses:
- no handshake
- no ACK
- direct data transfer

---

# 📸 Screenshot

| Python UDP DNS Traffic Analysis | [Open](https://github.com/user-attachments/assets/d2e0936b-8f7a-4348-aba8-589bcc976f5e) |

---

# 💼 Real-World Use Cases

Concepts used in:
- SOC analysis
- DNS monitoring
- malware traffic analysis
- DNS tunneling detection
- network forensics
- threat hunting
- traffic inspection

---

# 📚 What Was Learned

- how UDP packets are structured
- how DNS traffic uses UDP
- how to extract source and destination IPs
- how to extract UDP ports
- how to identify port 53 DNS traffic
- how UDP differs from TCP
- why DNS traffic is important in cybersecurity

---

# ⚠️ Disclaimer

This project is intended for educational purposes only.

All activities were performed in controlled lab environments.
