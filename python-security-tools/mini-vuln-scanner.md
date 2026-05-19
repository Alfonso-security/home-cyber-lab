# 🛡️ Python Mini Vulnerability Scanner

This project demonstrates how to build a basic vulnerability-oriented scanner using Python sockets.

The script:
- scans multiple ports
- performs banner grabbing
- identifies service versions
- checks for potentially vulnerable software versions

---

# 📌 Objective

Understand:
- TCP scanning
- service enumeration
- banner grabbing
- fingerprinting
- version matching
- basic vulnerability assessment
- Python networking

---

# 📂 File

| File | Description |
|---|---|
| `mini-vuln-scanner.py` | Basic vulnerability-oriented scanner |

---

# 🐍 Python Code

```python
import socket

TARGET = input("Enter target IP: ")

print(f"\nScanning target: {TARGET}\n")

VULNERABLE_BANNERS = [
    "OpenSSH_6",
    "Apache/2.2",
    "vsFTPd 2.3.4"
]

for port in [21,22,80,8080]:

    try:

        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        scanner.settimeout(2)

        result = scanner.connect_ex((TARGET, port))

        if result == 0:

            print(f"[+] Port {port} OPEN")

            if port == 80 or port == 8080:

                request = "HEAD / HTTP/1.0\r\n\r\n"

                scanner.send(request.encode())

            banner = scanner.recv(1024).decode(errors="ignore")

            print(f"[BANNER] {banner}")

            for vuln in VULNERABLE_BANNERS:

                if vuln in banner:

                    print(f"[!] Possible vulnerable service detected: {vuln}")

        scanner.close()

    except:
        pass
```

---

# 📌 Code Explanation

---

# Import socket library

```python
import socket
```

Imports the Python networking library.

Mental model:

```text
socket = network communication endpoint
```

---

# User input

```python
TARGET = input("Enter target IP: ")
```

Allows the user to enter:
- IP address
- hostname

Examples:

```text
127.0.0.1
scanme.nmap.org
example.com
```

Mental model:

```text
TARGET = destination computer/server
```

---

# Vulnerable banners list

```python
VULNERABLE_BANNERS = [
    "OpenSSH_6",
    "Apache/2.2",
    "vsFTPd 2.3.4"
]
```

This list contains example service versions that may be vulnerable.

Mental model:

```text
known suspicious software versions
```

---

# Port list

```python
for port in [21,22,80,8080]:
```

Scans multiple service ports.

| Port | Service |
|---|---|
| 21 | FTP |
| 22 | SSH |
| 80 | HTTP |
| 8080 | Alternative HTTP |

Mental model:

```text
check multiple service doors
```

---

# Try block

```python
try:
```

Attempts safe execution.

Mental translation:

```text
try = prova
(try)
```

---

# Create socket

```python
scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Creates a TCP IPv4 socket.

| Part | Meaning |
|---|---|
| `AF_INET` | IPv4 |
| `SOCK_STREAM` | TCP |

Mental model:

```text
create a network phone
```

---

# Timeout

```python
scanner.settimeout(2)
```

Sets maximum waiting time to 2 seconds.

Mental translation:

```text
timeout = maximum waiting time
```

---

# TCP connection

```python
result = scanner.connect_ex((TARGET, port))
```

Attempts TCP connection to target port.

Mental model:

```text
knock on a network door
```

---

# Open port check

```python
if result == 0:
```

If the connection succeeds:
- the port is open
- a service is listening

Mental model:

```text
someone answered the door
```

---

# HTTP request

```python
request = "HEAD / HTTP/1.0\r\n\r\n"
```

Creates a minimal HTTP request.

`HEAD` requests:
- headers only
- no webpage body

Mental model:

```text
tell me who you are without sending everything
```

---

# Send request

```python
scanner.send(request.encode())
```

Sends request as bytes.

Mental translation:

```text
encode = convert readable text into bytes
```

---

# Receive banner

```python
banner = scanner.recv(1024).decode(errors="ignore")
```

Receives and decodes server response.

| Function | Meaning |
|---|---|
| `recv()` | receive data |
| `decode()` | convert bytes into readable text |

Mental model:

```text
server identity card
```

---

# Print banner

```python
print(f"[BANNER] {banner}")
```

Displays service information.

Example:

```text
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu
```

---

# Version matching

```python
if vuln in banner:
```

Checks if a known vulnerable version exists inside the banner.

Mental model:

```text
compare identity card against suspicious versions
```

---

# Vulnerability alert

```python
print(f"[!] Possible vulnerable service detected: {vuln}")
```

Displays warning message.

Important:
this does NOT confirm a real vulnerability.

It only identifies:
- potentially outdated software
- known vulnerable versions

---

# Close socket

```python
scanner.close()
```

Closes the network connection.

Mental model:

```text
hang up the network phone
```

---

# 🚀 Practical Test

## Run scanner

```bash
python3 mini-vuln-scanner.py
```

---

# Example Target

```text
scanme.nmap.org
```

---

# Example Result

```text
[+] Port 22 OPEN

[BANNER]
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13

[!] Possible vulnerable service detected: OpenSSH_6
```

---

# 📸 Screenshot

<img width="1263" height="768" alt="Screenshot 2026-05-19 214205" src="https://github.com/user-attachments/assets/955c9df9-26aa-446b-97dd-d38d832a5263" />


---

# 💼 Real-World Use Cases

This type of logic is used in:

- vulnerability assessment
- penetration testing
- attack surface analysis
- SOC investigations
- service auditing
- asset discovery
- infrastructure analysis

---

# 🧠 Mental Networking Model

```text
TARGET = building
port = room
service = person inside room
banner = identity card
scanner = investigator
version matching = compare against suspicious list
```

---

# 📚 What Was Learned

- how TCP scanners work
- how banner grabbing works
- how services expose version information
- how version matching works
- how basic vulnerability identification works
- how sockets communicate
- how scanners identify services

---

# ⚠️ Disclaimer

This project is intended for educational purposes only.

All activities were performed in controlled lab environments.
