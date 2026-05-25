# 🌐 Python HTTP Traffic Parser

This project demonstrates how to capture and analyze HTTP traffic using Python raw sockets.

The script extracts:
- source IP
- destination IP
- source port
- destination port
- HTTP payload data

This allows inspection of:
- HTTP GET requests
- HTTP headers
- Host values
- User-Agent strings
- web traffic behavior

---

# 📌 Objective

Understand:
- HTTP traffic analysis
- TCP payload extraction
- web request inspection
- application-layer protocols
- raw packet analysis
- HTTP headers
- web communication

---

# 📂 File

| File | Description |
|---|---|
| `http-parser.py` | HTTP traffic parser and analyzer |

---

# 🐍 Python Code

```python
import socket
import struct

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Listening for HTTP traffic...\n")

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

            if destination_port == 80 or source_port == 80:

                data = raw_data[54:]

                try:

                    http_data = data.decode(errors="ignore")

                    print("\n[HTTP TRAFFIC]")
                    print(f"Source IP: {source_ip}:{source_port}")
                    print(f"Destination IP: {destination_ip}:{destination_port}")

                    print(http_data[:500])

                except:
                    pass
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

---

# Ethernet unpacking

```python
eth = struct.unpack("!6s6sH", ethernet_header)
```

Interprets Ethernet frame structure.

---

# IPv4 detection

```python
if protocol == 8:
```

Checks if packet contains IPv4 traffic.

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

Interprets IPv4 fields.

Contains:
- source IP
- destination IP
- protocol
- TTL

---

# Source and destination IP

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

# TCP detection

```python
if ip_protocol == 6:
```

Checks if packet contains TCP traffic.

---

# TCP header extraction

```python
tcp_header = raw_data[34:54]
```

Extracts TCP header.

Contains:
- source port
- destination port
- TCP flags
- sequence numbers

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
IP = device
port = service
```

---

# HTTP traffic detection

```python
if destination_port == 80 or source_port == 80:
```

Checks for HTTP traffic.

Port `80` is the standard HTTP port.

---

# HTTP payload extraction

```python
data = raw_data[54:]
```

Extracts application-layer data.

Mental model:

```text
Ethernet Header
↓

IP Header
↓

TCP Header
↓

HTTP Data
```

---

# HTTP decoding

```python
http_data = data.decode(errors="ignore")
```

Converts HTTP bytes into readable text.

Mental translation:

```text
decode = bytes → readable text
```

---

# HTTP data printing

```python
print(http_data[:500])
```

Displays the first 500 characters of HTTP traffic.

---

# 🚀 Practical Test

## Run parser

```bash
sudo python3 http-parser.py
```

⚠️ Root privileges required.

---

# Generate HTTP Traffic

Open another terminal:

```bash
curl http://example.com
```

or open:

```text
http://example.com
```

⚠️ Use HTTP and not HTTPS.

---

# Example Output

```http
GET / HTTP/1.1
Host: example.com
User-Agent: curl/8.0
Accept: */*
```

---

# 📌 Important Concept

HTTP traffic:
- is readable
- is not encrypted
- can be inspected directly

HTTPS traffic:
- is encrypted
- cannot be read directly from packet payload

Mental model:

```text
HTTP = readable conversation

HTTPS = encrypted conversation
```

---

# 📸 Screenshot

| Python Http Traffic Analysis | [Open](https://github.com/user-attachments/assets/05705596-edda-4fcd-bd48-1164b99a1d28) |

---

# 💼 Real-World Use Cases

Concepts used in:
- SOC investigations
- proxy inspection
- malware traffic analysis
- phishing analysis
- IDS/IPS
- web traffic monitoring
- threat hunting

---

# 📚 What Was Learned

- how HTTP traffic works
- how web requests are structured
- how to extract HTTP payloads
- how to identify HTTP traffic
- how TCP transports web traffic
- why HTTP traffic is readable
- difference between HTTP and HTTPS

---

# 🧠 Mental Networking Model

```text
TCP = transport layer

HTTP = application conversation
```

---

# ⚠️ Disclaimer

This project is intended for educational purposes only.

All activities were performed in controlled lab environments.
