# 🛡️ Python Safe Port Scanner

This project shows how to create a safer TCP port scanner in Python using:
- socket programming
- timeout management
- error handling
- user input

The scanner can detect open TCP ports while handling connection and hostname errors correctly.

---

# 📌 Objective

Understand:
- TCP port scanning
- Python sockets
- error handling
- user input
- hostname resolution
- timeout management
- basic reconnaissance

---

# 📂 File

| File | Description |
|---|---|
| `safe-port-scanner.py` | TCP scanner with error handling |

---

# 🐍 Python Code

```python
import socket

TARGET = input("Enter target IP: ")

print(f"\nScanning target: {TARGET}\n")

for port in range(75, 85):

    try:

        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        scanner.settimeout(0.05)

        result = scanner.connect_ex((TARGET, port))

        if result == 0:
            print(f"[+] Port {port} OPEN")

        scanner.close()

    except socket.gaierror:
        print("Hostname could not be resolved")
        break

    except socket.error:
        print("Could not connect to server")
        break
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

This asks the user to enter a target IP or hostname.

Example:

```text
127.0.0.1
scanme.nmap.org
```

Mental model:

```text
input = ask user for information
```

---

# Print target

```python
print(f"\nScanning target: {TARGET}\n")
```

Displays the target currently being scanned.

`f-string` allows variables inside text.

---

# Port range

```python
for port in range(75, 85):
```

Scans ports:

```text
75 → 84
```

The second number is excluded.

Mental model:

```text
check multiple doors automatically
```

---

# Try block

```python
try:
```

Python attempts to execute the code safely.

Mental translation:

```text
try = prova
(try)
```

---

# Socket creation

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
scanner.settimeout(0.05)
```

Sets maximum waiting time to `0.05` seconds.

Meaning:

```text
do not wait too long for a response
```

Mental translation:

```text
timeout = maximum waiting time
```

---

# TCP connection test

```python
result = scanner.connect_ex((TARGET, port))
```

Attempts a TCP connection to the target port.

`connect_ex()` returns a number instead of crashing.

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

If the result is `0`, the port is open.

Meaning:

```text
a service is listening on that port
```

---

# Print open port

```python
print(f"[+] Port {port} OPEN")
```

Displays detected open ports.

Example:

```text
[+] Port 80 OPEN
```

---

# Close socket

```python
scanner.close()
```

Closes the socket after testing.

This prevents resource accumulation.

Mental model:

```text
hang up the network phone
```

---

# Exception handling

```python
except socket.gaierror:
```

Handles hostname resolution errors.

Example:

```text
wrong hostname
invalid domain
```

Mental translation:

```text
exception = error handling
```

---

# Socket error

```python
except socket.error:
```

Handles network connection errors.

Example:
- network unreachable
- server unavailable
- firewall issues

---

# Break

```python
break
```

Stops the loop immediately.

Mental translation:

```text
break = stop the loop
```

---

# 🚀 Practical Test

## Start Netcat Listener

```bash
nc -lvnp 80
```

This opens a TCP listener on port `80`.

Mental model:

```text
open a listening service
```

---

# Run Scanner

```bash
python3 safe-port-scanner.py
```

---

# Enter Target

```text
127.0.0.1
```

---

# Example Result

```text
Scanning target: 127.0.0.1

[+] Port 80 OPEN
```

---

# 📸 Screenshot

<img width="1251" height="767" alt="Screenshot 2026-05-19 195800" src="https://github.com/user-attachments/assets/11a4477e-7935-41b5-a103-e0933a53785f" />

---

# 💼 Real-World Use Cases

This script can be useful for:

- service discovery
- network troubleshooting
- checking open ports
- vulnerability assessment
- SOC learning
- cybersecurity labs
- basic reconnaissance

---

# 🧠 Mental Networking Model

```text
IP = building
port = room
service = person inside the room
scanner = person knocking on doors
listener = person answering the door
```

---

# 📚 What Was Learned

- how TCP scanners work
- how sockets work
- how timeout improves scanning
- how error handling works
- how services create open ports
- how listeners work
- how scanners detect active services

---

# ⚠️ Disclaimer

This project is intended for educational purposes only.

All activities were performed in controlled lab environments.
