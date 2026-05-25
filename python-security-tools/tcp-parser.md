# 🌐 Python TCP Packet Parser

This project demonstrates how to capture and analyze TCP packets using Python raw sockets.

The script extracts:
- source IP
- destination IP
- source port
- destination port
- TCP flags

This allows basic TCP traffic analysis and handshake inspection.

---

# 📌 Objective

Understand:
- TCP packet parsing
- TCP flags
- TCP handshake
- packet analysis
- network traffic monitoring
- raw socket parsing
- protocol analysis

---

# 📂 File

| File | Description |
|---|---|
| `tcp-parser.py` | TCP packet parser and analyzer |

---

# 🐍 Python Code

```python
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
```

---

# 📌 Code Explanation

---

# Import libraries

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
socket = network communication

struct = binary packet interpreter
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

Allows direct access to packets on Linux.

Mental translation:

```text
packet-level access
```

---

# `SOCK_RAW`

```python
socket.SOCK_RAW
```

Captures raw network traffic.

Mental translation:

```text
raw = grezzo
(raw)
```

Meaning:

```text
capture packets without automatic interpretation
```

---

# `socket.ntohs(3)`

Captures all Ethernet protocols.

Mental translation:

```text
convert network byte order into readable host format
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

# Receive packets

```python
raw_data, addr = sniffer.recvfrom(65535)
```

Captures:
- raw packet bytes
- source information

---

# Ethernet header extraction

```python
ethernet_header = raw_data[0:14]
```

Extracts Ethernet frame header.

Contains:
- source MAC
- destination MAC
- protocol type

---

# Ethernet unpacking

```python
eth = struct.unpack("!6s6sH", ethernet_header)
```

Interprets Ethernet frame structure.

Mental translation:

```text
unpack = spacchetta dati
(unpack data)
```

---

# Protocol extraction

```python
protocol = socket.htons(eth[2])
```

Extracts Ethernet protocol type.

Example:

```text
8 = IPv4
```

---

# IPv4 detection

```python
if protocol == 8:
```

Checks if packet is IPv4.

---

# IP header extraction

```python
ip_header = raw_data[14:34]
```

Extracts IPv4 header.

---

# IP unpacking

```python
iph = struct.unpack("!BBHHHBBH4s4s", ip_header)
```

Interprets IPv4 header fields.

Contains:
- source IP
- destination IP
- protocol type
- TTL

---

# IP extraction

```python
source_ip = socket.inet_ntoa(iph[8])

destination_ip = socket.inet_ntoa(iph[9])
```

Converts binary IP into readable format.

Mental translation:

```text
inet_ntoa = binary IP → readable IP
```

---

# Protocol identification

```python
ip_protocol = iph[6]
```

Extracts IP protocol.

| Value | Protocol |
|---|---|
| `6` | TCP |
| `17` | UDP |
| `1` | ICMP |

---

# TCP packet detection

```python
if ip_protocol == 6:
```

Checks if packet contains TCP traffic.

Mental model:

```text
only analyze TCP packets
```

---

# TCP header extraction

```python
tcp_header = raw_data[34:54]
```

Extracts TCP header.

Contains:
- ports
- sequence numbers
- flags

---

# TCP unpacking

```python
tcph = struct.unpack("!HHLLBBHHH", tcp_header)
```

Interprets TCP header fields.

---

# Port extraction

```python
source_port = tcph[0]

destination_port = tcph[1]
```

Extracts TCP ports.

Mental model:

```text
which services are communicating
```

---

# TCP Flags

```python
flags = tcph[5]
```

Extracts TCP flags.

TCP flags describe connection state.

---

# Common TCP Flags

| Value | Meaning |
|---|---|
| `2` | SYN |
| `16` | ACK |
| `18` | SYN + ACK |
| `24` | PSH + ACK |

---

# TCP Handshake Mental Model

```text
SYN
"can I connect?"

↓

SYN ACK
"yes I hear you"

↓

ACK
"connection established"
```

---

# Data transfer

```text
PSH ACK
"send application data"
```

---

# Print packet information

```python
print(f"Source IP: {source_ip}:{source_port}")
print(f"Destination IP: {destination_ip}:{destination_port}")
print(f"Flags: {flags}")
```

Displays:
- IP addresses
- TCP ports
- connection state

---

# 🚀 Practical Test

## Run parser

```bash
sudo python3 tcp-parser.py
```

⚠️ Root privileges required.

---

# Generate TCP Traffic

Open another terminal:

```bash
curl google.com
```

or:

```bash
firefox
```

---

# Example Output

```text
[TCP PACKET]
Source IP: 10.0.2.15:44924
Destination IP: 172.x.x.x:80
Flags: 2
```

---

# Example TCP Flow

| Flags | Meaning |
|---|---|
| `2` | SYN |
| `18` | SYN ACK |
| `16` | ACK |
| `24` | PSH ACK |

---

# 📸 Screenshot

| Python Tcp Packet Analysis | [Open](https://github.com/user-attachments/assets/d8dfb3bb-c0e1-410d-ae97-5514432a0838) |
---

# 💼 Real-World Use Cases

Concepts used in:
- Wireshark
- IDS/IPS
- network forensics
- SOC analysis
- malware traffic analysis
- TCP troubleshooting
- threat hunting

---

# 🧠 Mental Networking Model

```text
TCP handshake = conversation setup

SYN = can I connect?
SYN ACK = yes
ACK = connection established
PSH ACK = data transfer
```

---

# 📚 What Was Learned

- how TCP packets work
- how TCP flags work
- how TCP handshake works
- how raw packet parsing works
- how services communicate
- how traffic analyzers inspect packets
- how TCP connections are established

---

# ⚠️ Disclaimer

This project is intended for educational purposes only.

All activities were performed in controlled lab environments.
