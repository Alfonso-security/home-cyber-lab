# 🌐 Python Reverse DNS Lookup

Questo progetto mostra come effettuare un reverse DNS lookup in Python utilizzando la libreria `socket`.

Il reverse DNS permette di ottenere il nome host associato a un indirizzo IP.

---

# 📌 Obiettivo

Comprendere:
- DNS
- reverse DNS
- hostname
- risoluzione nomi
- networking Python
- utilizzo di `socket.gethostbyaddr()`

---

# 📂 File

| File | Descrizione |
|---|---|
| reverse-dns.py | reverse DNS lookup Python |

---

# 🐍 Codice Python

```python
import socket

TARGET = "8.8.8.8"

hostname = socket.gethostbyaddr(TARGET)

print(f"Hostname: {hostname[0]}")
```

---

# 📌 Spiegazione del codice

## Import libreria socket

```python
import socket
```

La libreria `socket` permette di utilizzare funzioni di networking in Python.

---

# 📌 Target IP

```python
TARGET = "8.8.8.8"
```

L'indirizzo IP utilizzato appartiene ai DNS pubblici Google.

---

# 📌 gethostbyaddr()

```python
socket.gethostbyaddr(TARGET)
```

Questa funzione esegue un reverse DNS lookup.

In pratica:

```text
IP → hostname
```

---

# 📌 Differenza tra DNS normale e reverse DNS

| Tipo | Funzione |
|---|---|
| DNS normale | dominio → IP |
| Reverse DNS | IP → hostname |

---

# 📌 Output completo

Output iniziale ottenuto:

```text
('dns.google', [], ['8.8.8.8'])
```

---

# 📌 Significato output

| Parte | Significato |
|---|---|
| `dns.google` | hostname principale |
| `[]` | eventuali alias |
| `['8.8.8.8']` | indirizzi IP associati |

---

# 📌 Accesso al primo elemento

```python
hostname[0]
```

Permette di ottenere solo il nome host principale.

---

# 📌 Output finale

```text
Hostname: dns.google
```

---

# 📌 Strutture dati Python

Il valore restituito da `gethostbyaddr()` è una tuple Python contenente più elementi.

---

# 📌 Indici Python

| Indice | Elemento |
|---|---|
| `[0]` | hostname |
| `[1]` | alias |
| `[2]` | lista IP |

---

# 🚀 Test effettuato

## Avvio script

```bash
python3 reverse-dns.py
```

---

# 📌 Risultato ottenuto

```text
Hostname: dns.google
```

---

# 📌 Cosa è stato imparato

- reverse DNS lookup
- hostname resolution
- utilizzo libreria socket
- networking Python
- tuple Python
- accesso agli elementi tramite indice

---

# 📸 Screenshot

<img width="1281" height="763" alt="Screenshot 2026-05-18 224334" src="https://github.com/user-attachments/assets/f89ca935-e2a2-446f-ad60-6f40717d875f" />

---

# 📚 Utilizzo pratico

Il reverse DNS lookup viene utilizzato in:
- cybersecurity
- SOC analysis
- SIEM
- log investigation
- threat intelligence
- incident response
- network analysis

---

# ⚠️ Disclaimer

Questo laboratorio è stato svolto esclusivamente per scopi educativi in ambiente controllato.
