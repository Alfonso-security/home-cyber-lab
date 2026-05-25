# 📡 Python ICMP Packet Parser

This project demonstrates how to capture and analyze ICMP packets using Python raw sockets.

The script extracts:
- source IP
- destination IP
- ICMP type
- ICMP code

This allows analysis of:
- ping requests
- ping replies
- network reachability
- ICMP diagnostics traffic

---

# 📌 Objective

Understand:
- ICMP packet parsing
- ping request/reply logic
- network diagnostics
- raw packet analysis
- protocol identification
- packet inspection
- network reachability

---

# 📂 File

| File | Description |
|---|---|
| `icmp-parser.py` | ICMP packet parser and analyzer |

---

# 🐍 Python Code

```python
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
struct = packet interpreter
```

---

# Raw socket creation

```python
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
```

Creates a raw packet sniffer.

Mental model:

```text
listen directly to network traffic
```

---

# Ethernet frame extraction

```python
ethernet_header = raw_data[0:14]
```

Extracts Ethernet header.

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
unpack = interpret binary data
```

---

# IPv4 detection

```python
if protocol == 8:
```

Checks if traffic contains IPv4 packets.

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

# Source and destination IP extraction

```python
source_ip = socket.inet_ntoa(iph[8])

destination_ip = socket.inet_ntoa(iph[9])
```

Converts binary IP addresses into readable format.

Mental translation:

```text
inet_ntoa = binary IP → readable IP
```

---

# Protocol identification

```python
ip_protocol = iph[6]
```

Extracts transport protocol.

| Value | Protocol |
|---|---|
| `1` | ICMP |
| `6` | TCP |
| `17` | UDP |

---

# ICMP detection

```python
if ip_protocol == 1:
```

Checks if packet contains ICMP traffic.

---

# ICMP header extraction

```python
icmp_header = raw_data[34:38]
```

Extracts ICMP header.

---

# ICMP unpacking

```python
icmph = struct.unpack("!BBH", icmp_header)
```

Interprets ICMP header fields.

| Field | Meaning |
|---|---|
| Type | ICMP message type |
| Code | subtype/error code |
| Checksum | integrity verification |

---

# ICMP Type

```python
icmp_type = icmph[0]
```

Indicates ICMP message category.

---

# Common ICMP Types

| Type | Meaning |
|---|---|
| `8` | Echo Request |
| `0` | Echo Reply |

---

# Mental model

```text
Type 8
"are you reachable?"

↓

Type 0
"yes I am reachable"
```

---

# ICMP Code

```python
code = icmph[1]
```

Provides additional ICMP information.

Usually:

```text
0
```

---

# Print packet information

```python
print(f"Source IP: {source_ip}")
print(f"Destination IP: {destination_ip}")
print(f"ICMP Type: {icmp_type}")
print(f"Code: {code}")
```

Displays:
- source IP
- destination IP
- ICMP packet type
- ICMP subtype

---

# 🚀 Practical Test

## Run parser

```bash
sudo python3 icmp-parser.py
```

⚠️ Root privileges required.

---

# Generate ICMP Traffic

Open another terminal:

```bash
ping google.com
```

---

# Example Output

```text
[ICMP PACKET]
Source IP: 10.0.2.15
Destination IP: 172.x.x.x
ICMP Type: 8
Code: 0
```

---

# Ping Reply Example

```text
[ICMP PACKET]
Source IP: 172.x.x.x
Destination IP: 10.0.2.15
ICMP Type: 0
Code: 0
```

---

# 📌 ICMP Flow

| ICMP Type | Meaning |
|---|---|
| `8` | Ping request |
| `0` | Ping reply |

---

# 🧠 Mental Networking Model

```text
ICMP request
"are you there?"

↓

ICMP reply
"yes I am here"
```

---

# 📸 Screenshot

| Python Real Icmp Ping Analysis | [Open](https://github.com/user-attachments/assets/c672759c-db21-4b14-bad5-7592c18f07cb) |

---

# 💼 Real-World Use Cases

Concepts used in:
- network diagnostics
- SOC investigations
- threat hunting
- traffic monitoring
- IDS/IPS
- network troubleshooting
- packet analysis

---

# 📚 What Was Learned

- how ICMP packets work
- how ping works internally
- how ICMP request/reply works
- how packet parsing works
- how to identify ICMP traffic
- how network diagnostics operate
- how raw packet analysis works

---

# ⚠️ Disclaimer

This project is intended for educational purposes only.

All activities were performed in controlled lab environments.
