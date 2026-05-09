# Listening Ports

## Obiettivo

Comprendere il funzionamento delle porte in ascolto e il loro ruolo nella cybersecurity.

---

# Cos’è una porta

Una porta è un punto di comunicazione utilizzato dai servizi di rete.

Ogni servizio utilizza:
- un protocollo
- una porta

Esempi:

| Porta | Servizio |
|---|---|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 53 | DNS |

---

# Listening Port

Una listening port è una porta in ascolto.

Significa che:
- un processo è attivo
- il servizio aspetta connessioni

---

# Stato LISTEN

```text
LISTEN
```
Indica:
```text
il servizio è pronto ad accettare connessioni
```
 Analogia
Una listening port è come:
```text
un telefono acceso che aspetta chiamate
```
# Comandi utilizzati
Visualizzare porte listening
```Bash
ss -tuln
```
## Significato opzioni

| Opzione | Significato      |
| ------- | ---------------- |
| t       | TCP              |
| u       | UDP              |
| l       | LISTEN           |
| n       | formato numerico |

Output esempio
```Bash
tcp LISTEN 0 5 0.0.0.0:8080
```
## Analisi output
| Campo   | Significato            |
| ------- | ---------------------- |
| tcp     | protocollo TCP         |
| LISTEN  | porta in ascolto       |
| 0.0.0.0 | accessibile dalla rete |
| 8080    | numero porta           |

## 127.0.0.1 vs 0.0.0.0
127.0.0.1
```text
servizio accessibile solo localmente
```
Più sicuro.

0.0.0.0
```text
servizio accessibile dalla rete
```
Più esposto.

## Visualizzare il processo associato
```Bash
ss -tulnp
```
## Significato opzione p
```text
p = process
```
Mostra quale processo sta utilizzando la porta.

# Esempio
```Bash
users:(("python3",pid=2100))
```
Significa che il processo python3 sta ascoltando sulla porta.

## Connessioni TCP attive
```Bash
ss -tanp
```
Mostra:

connessioni ESTABLISHED

processi

IP remoti

porte remote

## ESTABLISHED
```text
ESTABLISHED
```
Significa:
```text
connessione TCP attiva
```
## Local Address

Indica:

IP locale

## Peer Address

Indica:

IP remoto

porta remota

porta locale

## Esempio reale
```Bash
ESTAB 10.0.2.15:52144 34.107.x.x:https
```
Significa:

la VM Kali Linux sta comunicando

tramite HTTPS

con un server remoto

## Creazione server locale
Avviare un server HTTP Python
```Bash
python3 -m http.server 8080
```
## Funzionamento
Il comando:

avvia un web server locale

apre la porta TCP 8080

mette il processo in listening

Verifica browser
```Bash
http://127.0.0.1:8080
```
# Concetti di cybersecurity appresi
listening ports

attack surface

processi rete

servizi in ascolto

porte TCP

connessioni ESTABLISHED

local address

peer address
