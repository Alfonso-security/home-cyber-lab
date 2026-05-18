# 🔎 Python Port Scanner

Questo progetto mostra la creazione di un semplice port scanner TCP in Python utilizzando la libreria `socket`.

---

# 📌 Obiettivo

Comprendere:
- socket TCP
- scansione porte
- networking in Python
- automazione base
- verifica porte aperte e chiuse

---

# 📂 File

| File | Descrizione |
|---|---|
| port-scanner.py | scanner porte TCP Python |

---

# 🐍 Codice Python

```python
import socket

TARGET = "127.0.0.1"
PORTS = [22, 80, 443, 7777, 8080]

for port in PORTS:

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(1)

    result = scanner.connect_ex((TARGET, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is CLOSED")

    scanner.close()
```

---

# 📌 Spiegazione del codice

## Import libreria socket

```python
import socket
```

La libreria `socket` permette di creare comunicazioni di rete in Python.

---

# 📌 Target

```python
TARGET = "127.0.0.1"
```

`127.0.0.1` rappresenta:
- localhost
- il computer locale

---

# 📌 Porte da analizzare

```python
PORTS = [22, 80, 443, 7777, 8080]
```

| Porta | Utilizzo comune |
|---|---|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 7777 | Netcat test |
| 8080 | Web alternative |

---

# 📌 Ciclo for

```python
for port in PORTS:
```

Il ciclo `for` analizza una porta alla volta.

---

# 📌 Creazione socket TCP

```python
scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

| Parametro | Significato |
|---|---|
| AF_INET | IPv4 |
| SOCK_STREAM | TCP |

---

# 📌 Timeout

```python
scanner.settimeout(1)
```

Imposta un timeout di 1 secondo.

Evita che il programma rimanga bloccato troppo a lungo.

---

# 📌 connect_ex()

```python
result = scanner.connect_ex((TARGET, port))
```

Tenta la connessione TCP alla porta specificata.

---

# 📌 Controllo risultato

```python
if result == 0:
```

| Valore | Significato |
|---|---|
| 0 | porta aperta |
| altro valore | porta chiusa |

---

# 📌 Chiusura socket

```python
scanner.close()
```

Chiude la connessione TCP.

---

# 🚀 Test effettuato

## Listener Netcat

```bash
nc -lvnp 7777
```

---

## Avvio scanner

```bash
python3 port-scanner.py
```

---

# 📌 Risultato ottenuto

```text
[-] Port 22 is CLOSED
[-] Port 80 is CLOSED
[-] Port 443 is CLOSED
[+] Port 7777 is OPEN
[-] Port 8080 is CLOSED
```

---

# 📌 Cosa è stato imparato

- scansione porte TCP
- networking Python
- socket programming
- localhost
- client/server communication
- automazione base

---

# 📸 Screenshot
<img width="1273" height="755" alt="Screenshot 2026-05-18 200404" src="https://github.com/user-attachments/assets/3ab17205-cd84-4b68-a1d6-231a8280df05" />

---

# 📚 Utilizzo pratico

Questi concetti sono utilizzati in:
- cybersecurity
- penetration testing
- network analysis
- SOC operations
- automation
- port enumeration
- vulnerability assessment
