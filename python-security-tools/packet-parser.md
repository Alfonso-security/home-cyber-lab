# 📦 Python Packet Parser

This project demonstrates how to parse raw network packets using Python.

The script captures raw traffic and extracts:
- Ethernet information
- source IP
- destination IP
- protocol data

This is one of the fundamental concepts behind:
- Wireshark
- IDS/IPS
- network forensics
- packet analyzers

---

# 📌 Objective

Understand:
- packet parsing
- Ethernet frames
- IP headers
- raw packet analysis
- binary data interpretation
- protocol extraction
- low-level networking

---

# 📂 File

| File | Description |
|---|---|
| `packet-parser.py` | Basic packet parser using raw sockets |

---

# 🐍 Python Code

```python
import socket
import struct

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Listening for packets...\n")

while True:

    raw_data, addr = sniffer.recvfrom(65535)

    ethernet_header = raw_data[0:14]

    eth = struct.unpack("!6s6sH", ethernet_header)

    protocol = socket.htons(eth[2])

    print(f"\n[ETHERNET FRAME]")
    print(f"Protocol: {protocol}")

    if protocol == 8:

        ip_header = raw_data[14:34]

        iph = struct.unpack("!BBHHHBBH4s4s", ip_header)

        source_ip = socket.inet_ntoa(iph[8])

        destination_ip = socket.inet_ntoa(iph[9])

        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {destination_ip}")
```

---

# 📌 Code Explanation

---

# Import socket library

```python
import socket
```

Provides networking functionality.

Mental model:

```text
socket = network communication endpoint
```

---

# Import struct library

```python
import struct
```

The `struct` module interprets raw binary data.

Mental translation:

```text
struct = structured binary interpreter
```

Mental model:

```text
open and interpret network packet structure
```

---

# Raw socket creation

```python
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
```

Creates a raw packet sniffer.

---

# `AF_PACKET`

```python
socket.AF_PACKET
```

Allows direct access to network packets on Linux.

Mental translation:

```text
packet-level networking access
```

---

# `SOCK_RAW`

```python
socket.SOCK_RAW
```

Creates a raw socket.

Meaning:

```text
capture traffic without automatic interpretation
```

Mental model:

```text
observe raw traffic directly from network card
```

---

# `socket.ntohs(3)`

```python
socket.ntohs(3)
```

Captures all Ethernet protocols.

Mental translation:

```text
network-to-host short conversion
```

Meaning:

```text
convert network byte order into readable system format
```

---

# Infinite listening loop

```python
while True:
```

Continuously listens for packets.

Mental translation:

```text
while = finché
(while)
```

---

# Receive packet

```python
raw_data, addr = sniffer.recvfrom(65535)
```

Captures:
- raw packet bytes
- source information

---

# `recvfrom()`

Mental translation:

```text
receive data from network
```

---

# `65535`

Maximum packet size.

Mental model:

```text
receive full packet
```

---

# Ethernet header extraction

```python
ethernet_header = raw_data[0:14]
```

Extracts the first 14 bytes of the Ethernet frame.

Ethernet header contains:
- source MAC
- destination MAC
- protocol type

---

# Packet unpacking

```python
eth = struct.unpack("!6s6sH", ethernet_header)
```

Interprets Ethernet header bytes.

Mental translation:

```text
unpack = spacchetta dati
(unpack data)
```

Mental model:

```text
open packet fields one by one
```

---

# Ethernet structure format

```python
"!6s6sH"
```

| Part | Meaning |
|---|---|
| `!` | network byte order |
| `6s` | 6-byte destination MAC |
| `6s` | 6-byte source MAC |
| `H` | protocol field |

---

# Protocol extraction

```python
protocol = socket.htons(eth[2])
```

Extracts protocol type.

Example:

```text
8 = IPv4
```

---

# IPv4 detection

```python
if protocol == 8:
```

Checks if packet contains IPv4 traffic.

Mental model:

```text
identify packet type before decoding
```

---

# IP header extraction

```python
ip_header = raw_data[14:34]
```

Extracts IPv4 header.

The IP header starts immediately after Ethernet header.

---

# IP unpacking

```python
iph = struct.unpack("!BBHHHBBH4s4s", ip_header)
```

Interprets IPv4 header fields.

This contains:
- version
- TTL
- protocol
- source IP
- destination IP

---

# Source IP extraction

```python
source_ip = socket.inet_ntoa(iph[8])
```

Converts binary IP into readable format.

Mental translation:

```text
inet_ntoa = binary IP → human-readable IP
```

---

# Destination IP extraction

```python
destination_ip = socket.inet_ntoa(iph[9])
```

Extracts destination IP address.

---

# Print packet information

```python
print(f"Source IP: {source_ip}")
print(f"Destination IP: {destination_ip}")
```

Displays readable packet information.

Example:

```text
Source IP: 192.168.1.10
Destination IP: 8.8.8.8
```

---

# 🧠 Important Concept

At this stage:
- raw bytes are being decoded
- packet structure is being interpreted
- network traffic becomes readable

Mental model:

```text
raw traffic → translated traffic
```

---

# 🚀 Practical Test

## Run parser

```bash
sudo python3 packet-parser.py
```

⚠️ Root privileges required.

---

# Generate Traffic

Open another terminal:

```bash
ping google.com
```

---

# Example Output

```text
[ETHERNET FRAME]
Protocol: 8

Source IP: 192.168.1.10
Destination IP: 8.8.8.8
```

---

# 📸 Screenshot

<img width="1271" height="764" alt="Screenshot 2026-05-19 221946" src="https://github.com/user-attachments/assets/03407a7b-238f-4d91-9fa5-db817421e556" />

---

# 💼 Real-World Use Cases

Concepts used in:
- Wireshark
- network forensics
- packet analyzers
- IDS/IPS
- SOC investigations
- malware analysis
- traffic monitoring

---

# 🧠 Mental Networking Model

```text
raw packet = closed box

packet parsing = opening and interpreting the box

protocol analysis = understanding what the packet contains
```

---

# 📚 What Was Learned

- how raw packet parsing works
- how Ethernet frames work
- how IP headers are structured
- how binary packet data becomes readable
- how packet analyzers work internally
- how protocols are identified
- how source and destination IPs are extracted

---

# ⚠️ Disclaimer

This project is intended for educational purposes only.

All activities were performed in controlled lab environments.
