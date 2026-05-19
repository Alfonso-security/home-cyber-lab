# 🌐 Python Multi Banner Grabber

This project shows how to perform basic service enumeration and banner grabbing using Python sockets.

The script scans multiple TCP ports and attempts to retrieve HTTP headers from web services.

---

# 📌 Objective

Understand:
- TCP service enumeration
- banner grabbing
- HTTP headers
- socket communication
- service fingerprinting
- basic reconnaissance
- Python networking

---

# 📂 File

| File | Description |
|---|---|
| `multi-banner-grabber.py` | Multi-port banner grabbing tool |

---

# 🐍 Python Code

```python
import socket

TARGET = input("Enter target IP: ")

print(f"\nScanning target: {TARGET}\n")

for port in [21,22,25,80,443,8080]:

    try:

        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        scanner.settimeout(1)

        result = scanner.connect_ex((TARGET, port))

        if result == 0:

            print(f"[+] Port {port} OPEN")

            if port == 80 or port == 8080:

                request = "HEAD / HTTP/1.0\r\n\r\n"

                scanner.send(request.encode())

                banner = scanner.recv(1024)

                print(banner.decode())

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

The `socket` library allows Python to create network communications.

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

---

# Print target

```python
print(f"\nScanning target: {TARGET}\n")
```

Displays the current target.

---

# Port list

```python
[21,22,25,80,443,8080]
```

These are common TCP service ports.

| Port | Service |
|---|---|
| 21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 80 | HTTP |
| 443 | HTTPS |
| 8080 | Alternative HTTP |

---

# Loop through ports

```python
for port in [21,22,25,80,443,8080]:
```

Scans multiple ports automatically.

Mental model:

```text
check multiple network doors
```

---

# Try block

```python
try:
```

Attempts to execute code safely.

Mental translation:

```text
try = prova
(try)
```

---

# Create TCP socket

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
scanner.settimeout(1)
```

Sets maximum waiting time to 1 second.

Mental translation:

```text
timeout = maximum waiting time
```

---

# Connection attempt

```python
result = scanner.connect_ex((TARGET, port))
```

Attempts a TCP connection to the target port.

| Result | Meaning |
|---|---|
| `0` | connection successful |
| non-zero | connection failed |

Mental model:

```text
knock on a network door
```

---

# Open port detection

```python
if result == 0:
```

Checks if the port is open.

Meaning:

```text
a service is listening
```

---

# HTTP request

```python
request = "HEAD / HTTP/1.0\r\n\r\n"
```

Creates a minimal HTTP request.

`HEAD` requests:
- headers only
- no full webpage body

Mental model:

```text
tell me who you are without sending the whole page
```

---

# Send request

```python
scanner.send(request.encode())
```

Sends the HTTP request.

Mental translation:

```text
encode = convert text into bytes
```

---

# Receive response

```python
banner = scanner.recv(1024)
```

Receives server response.

`1024` =
maximum number of bytes to receive.

Mental translation:

```text
recv = receive data
```

---

# Decode response

```python
print(banner.decode())
```

Converts bytes into readable text.

Mental translation:

```text
decode = convert bytes into readable text
```

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

## Run script

```bash
python3 multi-banner-grabber.py
```

---

# Example target

```text
scanme.nmap.org
```

or:

```text
example.com
```

---

# Example Result

```text
[+] Port 80 OPEN

HTTP/1.1 200 OK
Server: Apache
Content-Type: text/html
```

---

# 📸 Screenshot

<img width="1271" height="761" alt="Screenshot 2026-05-19 204711" src="https://github.com/user-attachments/assets/0684dee0-8d77-4f36-91b7-6277967393db" />
---

# 💼 Real-World Use Cases

This type of script is useful for:

- service fingerprinting
- reconnaissance
- vulnerability assessment
- asset discovery
- penetration testing labs
- SOC investigations
- troubleshooting

---

# 🧠 Mental Networking Model

```text
IP = building
port = room
service = person inside the room
scanner = person knocking on doors
banner = service identification card
```

---

# 📚 What Was Learned

- how banner grabbing works
- how HTTP headers work
- how TCP service enumeration works
- how sockets communicate
- how services identify themselves
- how Python handles network requests
- how bytes and strings are converted

---

# ⚠️ Disclaimer

This project is intended for educational purposes only.

All activities were performed in controlled lab environments.
