# 🐍 Python TCP Client

Questo script Python crea una connessione TCP verso un server locale utilizzando la libreria `socket`.

---

# 📌 Obiettivo

Comprendere:
- socket TCP
- comunicazione client/server
- networking in Python
- invio dati tramite TCP

---

# 📌 Libreria utilizzata

```python
import socket
```

La libreria `socket` permette di creare comunicazioni di rete in Python.

---

# 📌 Configurazione server

```python
HOST = "127.0.0.1"
PORT = 7777
```

| Campo | Significato |
|---|---|
| 127.0.0.1 | localhost |
| 7777 | porta TCP utilizzata |

---

# 📌 Creazione socket TCP

```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

| Parte | Significato |
|---|---|
| AF_INET | IPv4 |
| SOCK_STREAM | TCP |

---

# 📌 Connessione TCP

```python
client.connect((HOST, PORT))
```

Il client si connette al server TCP.

---

# 📌 Invio messaggio

```python
client.send(MESSAGE.encode())
```

La stringa viene convertita in bytes tramite `.encode()` prima dell'invio.

---

# 📌 Chiusura connessione

```python
client.close()
```

Chiude il socket TCP.

---

# 📌 Test effettuato

## Listener Netcat

```bash
nc -lvnp 7777
```

## Esecuzione script Python

```bash
python3 tcp-client.py
```

---

# 📌 Cosa è stato osservato

- connessione TCP localhost
- invio dati tramite Python
- ricezione messaggio tramite Netcat
- comunicazione client/server reale

---

# 📌 Utilizzo pratico

Questi concetti sono utilizzati in:
- networking
- cybersecurity
- socket programming
- automation
- penetration testing
- malware analysis

---

# 📸 Screenshot
<img width="1274" height="755" alt="Screenshot 2026-05-12 171120" src="https://github.com/user-attachments/assets/19ad5ae9-2650-4469-be33-9955e207cba1" />
