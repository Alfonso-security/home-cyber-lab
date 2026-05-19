# 🕵️ Python Packet Sniffer

This project demonstrates how to capture raw network packets using Python raw sockets.

The script listens directly to network traffic and displays raw packet data in real time.

---

# 📌 Objective

Understand:
- packet sniffing
- raw sockets
- network traffic analysis
- packet capture
- Ethernet frames
- low-level networking
- packet parsing concepts

---

# 📂 File

| File | Description |
|---|---|
| `python-packet-sniffer.py` | Basic raw packet sniffer |

---

# 🐍 Python Code

```python
import socket

sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Listening for packets...\n")

while True:

    raw_data, addr = sniffer.recvfrom(65535)

    print(raw_data)
```

---

# 📌 Code Explanation

---

# Import socket library

```python
import socket
```

Imports Python networking functions.

Mental model:

```text
socket = network communication endpoint
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

Linux low-level packet interface.

Mental translation:

```text
direct packet access
```

Mental model:

```text
read packets directly from network card
```

---

# `SOCK_RAW`

```python
socket.SOCK_RAW
```

Creates a raw socket.

Mental translation:

```text
raw = grezzo
(raw)
```

Meaning:

```text
do not interpret traffic automatically
```

---

# `socket.ntohs(3)`

```python
socket.ntohs(3)
```

Captures all Ethernet protocols.

Mental translation:

```text
network to host short
```

This converts network byte order into readable host format.

Mental model:

```text
translate network language into local system language
```

---

# Infinite loop

```python
while True:
```

Keeps listening forever.

Mental translation:

```text
while = finché
(while)
```

Meaning:

```text
keep sniffing packets continuously
```

---

# Receive packets

```python
raw_data, addr = sniffer.recvfrom(65535)
```

Receives:
- packet data
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
receive complete network packet
```

---

# Print raw data

```python
print(raw_data)
```

Displays captured raw packet bytes.

Example:

```text
b'\xff\xff\xff\xff...'
```

These are:
- raw bytes
- undecoded packet data

---

# 🧠 Important Concept

At this stage:
- packets are still undecoded
- data is raw
- traffic is not yet human-readable

Mental model:

```text
closed network boxes
```

The next step in packet analysis is:
- packet parsing
- protocol decoding
- header analysis

---

# 🚀 Practical Test

## Run Sniffer

```bash
sudo python3 python-packet-sniffer.py
```

⚠️ Root privileges are required.

---

# Generate Traffic

Open another terminal:

```bash
ping google.com
```

---

# Example Output

```text
b'\xff\xff\xff\xff...'
```

Raw packet bytes will continuously appear.

---

# 📸 Screenshot

<img width="1263" height="758" alt="Screenshot 2026-05-19 221137" src="https://github.com/user-attachments/assets/2deb14e8-2b0a-4a6f-a29e-1cbafbafbeea" />


---

# 💼 Real-World Use Cases

Concepts used in:
- Wireshark
- IDS/IPS
- network forensics
- malware analysis
- SOC investigations
- traffic monitoring
- packet analysis

---

# 🧠 Mental Networking Model

```text
scanner = knocks on doors
sniffer = listens to network traffic
```

---

# 📚 What Was Learned

- how raw sockets work
- how packet sniffing works
- how network traffic is captured
- how low-level networking works
- how raw packet bytes look
- why packet parsing is necessary
- how packet analysis tools begin working

---

# ⚠️ Disclaimer

This project is intended for educational purposes only.

All activities were performed in controlled lab environments.
