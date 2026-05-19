# 🔍 Python Multi Port Scanner

This project shows how to build a simple multi-port TCP scanner in Python using the `socket` library.

The scanner automatically checks multiple ports on a target host and identifies open TCP services.

---

# 📌 Objective

Understand:
- TCP port scanning
- socket programming
- automated port enumeration
- loops and ranges in Python
- timeout management
- TCP connection testing
- basic reconnaissance concepts

---

# 📂 File

| File | Description |
|---|---|
| `multi-port-scanner.py` | Multi-port TCP scanner |

---

# 🐍 Python Code

```python
import socket

TARGET = "127.0.0.1"

print(f"Scanning target: {TARGET}")

for port in range(7700, 7800):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(0.1)

    result = scanner.connect_ex((TARGET, port))

    if result == 0:
        print(f"[+] Port {port} OPEN")

    scanner.close()
```

---

# 📌 Explanation of the Code

---

# Import socket library

```python
import socket
```

The `socket` library allows Python to create network communications.

Sockets are used to connect systems and services over a network.

---

# Target definition

```python
TARGET = "127.0.0.1"
```

The scanner targets the localhost machine.

`127.0.0.1` is the IPv4 localhost address.

This means the script scans the same machine where it is executed.

---

# Output message

```python
print(f"Scanning target: {TARGET}")
```

This line displays the current scanning target.

The `f` before the string creates an f-string, allowing variables to be inserted directly inside the text.

---

# Range function

```python
range(7700, 7800)
```

This generates a sequence of ports from:

```text
7700 → 7799
```

The second value is excluded.

---

# Why use a smaller range?

Scanning all ports from 1 to 65535 would take much longer.

A smaller range is useful for:
- testing
- local labs
- troubleshooting
- faster scans

---

# Socket creation

```python
scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

This creates a TCP socket.

| Component | Meaning |
|---|---|
| `AF_INET` | IPv4 |
| `SOCK_STREAM` | TCP communication |

---

# Timeout management

```python
scanner.settimeout(0.1)
```

This sets the maximum waiting time to 0.1 seconds.

If the target port does not respond within that time, Python stops waiting and continues.

This makes the scanner much faster.

---

# Why is timeout important?

Without timeout:
- scans become very slow
- closed ports may delay execution
- filtered ports may freeze the scanner

---

# TCP connection test

```python
result = scanner.connect_ex((TARGET, port))
```

`connect_ex()` attempts a TCP connection to the target port.

Unlike `connect()`, this function returns an error code instead of crashing.

---

# Result values

| Result | Meaning |
|---|---|
| `0` | connection successful |
| non-zero | connection failed |

---

# Open port detection

```python
if result == 0:
```

If the result equals `0`, the TCP connection succeeded.

This means:
- the port is open
- a service is listening

---

# Output example

```python
print(f"[+] Port {port} OPEN")
```

Example output:

```text
[+] Port 7777 OPEN
```

---

# Socket closing

```python
scanner.close()
```

This closes the socket after each scan attempt.

Closing sockets is important to:
- free resources
- avoid connection accumulation
- prevent networking issues

---

# 🚀 Practical Test

## Netcat Listener

```bash
nc -lvnp 7777
```

This creates a TCP listener on port `7777`.

---

# Scanner Execution

```bash
python3 multi-port-scanner.py
```

---

# Example Result

```text
Scanning target: 127.0.0.1
[+] Port 7777 OPEN
```

---

# 📌 What Was Learned

- TCP port scanning
- automated port enumeration
- Python loops
- Python ranges
- timeout handling
- socket programming
- open port detection
- localhost scanning
- reconnaissance basics

---

# 📸 Screenshot

<img width="1262" height="460" alt="Screenshot 2026-05-19 171117" src="https://github.com/user-attachments/assets/9a956544-5b01-44c0-aca8-a1e8b63c3f84" />

---

# 📚 Real-World Usage

Port scanners are commonly used in:
- cybersecurity
- network administration
- vulnerability assessment
- troubleshooting
- penetration testing
- service discovery
- SOC operations

---

# ⚠️ Disclaimer

This laboratory activity was performed exclusively in a controlled environment for educational purposes.
