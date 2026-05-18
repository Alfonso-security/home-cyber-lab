# 🛰️ Python Banner Grabber

Questo progetto mostra come creare un semplice banner grabber in Python utilizzando la libreria `socket`.

Il banner grabbing serve a recuperare informazioni da un servizio remoto, ad esempio header HTTP, nome server, tipo contenuto e altre informazioni utili per analisi di rete e cybersecurity.

---

# 📌 Obiettivo

Comprendere:
- socket programming
- connessioni verso servizi remoti
- richieste HTTP manuali
- recupero header HTTP
- banner grabbing
- analisi base dei servizi

---

# 📂 File

| File | Descrizione |
|---|---|
| `banner-grabber.py` | Script Python per recuperare header HTTP da un server |

---

# 🐍 Codice Python

```python
import socket

TARGET = "scanme.nmap.org"
PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.settimeout(3)

client.connect((TARGET, PORT))

request = "HEAD / HTTP/1.0\r\n\r\n"

client.send(request.encode())

banner = client.recv(1024)

print(banner.decode())

client.close()
```

---

# 📌 Spiegazione del codice

## Import della libreria socket

```python
import socket
```

La libreria `socket` permette a Python di creare comunicazioni di rete.

In pratica, una socket è un punto di comunicazione tra due programmi.

---

## Target e porta

```python
TARGET = "scanme.nmap.org"
PORT = 80
```

`TARGET` indica il server da contattare.

`PORT` indica la porta del servizio da interrogare.

In questo caso viene usata la porta `80`, cioè il servizio HTTP.

---

## Creazione della socket

```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Questa riga crea una socket per comunicare con il server.

| Parte | Significato |
|---|---|
| `socket.socket()` | crea una nuova socket |
| `AF_INET` | usa indirizzi IPv4 |
| `SOCK_STREAM` | usa una comunicazione TCP |

---

## Timeout

```python
client.settimeout(3)
```

Questa riga imposta un limite massimo di attesa di 3 secondi.

Serve per evitare che il programma resti bloccato se:
- il server non risponde
- la porta è filtrata
- la connessione è troppo lenta
- il servizio non è disponibile

---

## Connessione al server

```python
client.connect((TARGET, PORT))
```

Questa riga apre una connessione verso il server e la porta indicati.

Se la connessione riesce, il programma può inviare e ricevere dati.

---

# 🌐 Richiesta HTTP manuale

```python
request = "HEAD / HTTP/1.0\r\n\r\n"
```

Questa è una richiesta HTTP scritta manualmente.

---

## Significato di HEAD

`HEAD` è un metodo HTTP.

Serve a chiedere al server solo gli header della risposta, senza scaricare il contenuto completo della pagina.

---

## Differenza tra HEAD e GET

| Metodo | Cosa riceve |
|---|---|
| `GET` | header + contenuto della pagina |
| `HEAD` | solo header |

---

## Significato di `/`

```text
/
```

Lo slash indica la root del sito.

Esempio:

```text
http://scanme.nmap.org/
```

---

## Significato di HTTP/1.0

```text
HTTP/1.0
```

Indica la versione del protocollo HTTP usata nella richiesta.

---

# 📌 Significato di `\r\n\r\n`

```python
"\r\n\r\n"
```

Questi sono caratteri speciali usati nei protocolli testuali come HTTP.

| Simbolo | Significato |
|---|---|
| `\r` | carriage return |
| `\n` | nuova riga |
| `\r\n` | fine riga HTTP |
| `\r\n\r\n` | fine degli header/richiesta |

---

## Perché servono?

HTTP usa righe separate da:

```text
\r\n
```

La doppia sequenza:

```text
\r\n\r\n
```

indica al server:

```text
la richiesta è finita
```

Se non viene inserita, il server potrebbe restare in attesa di altri dati.

---

# 📤 Invio della richiesta

```python
client.send(request.encode())
```

Questa riga invia la richiesta HTTP al server.

`.encode()` converte il testo in bytes, perché la rete trasmette bytes e non stringhe Python.

---

# 📥 Ricezione della risposta

```python
banner = client.recv(1024)
```

Questa riga riceve fino a 1024 byte di risposta dal server.

Il risultato viene salvato nella variabile `banner`.

---

# 📌 Conversione della risposta

```python
print(banner.decode())
```

`recv()` restituisce dati in formato bytes.

`.decode()` converte i bytes in testo leggibile.

---

# 🔚 Chiusura della connessione

```python
client.close()
```

Questa riga chiude la connessione.

È importante chiudere sempre le socket dopo l’uso.

---

# 📌 Header e Body

Una risposta HTTP è composta da:

```text
HEADER + BODY
```

---

## Header

Gli header contengono informazioni sulla risposta.

Esempi:

```text
HTTP/1.1 200 OK
Server: Apache
Content-Type: text/html
Content-Length: 1234
```

---

## Body

Il body contiene il contenuto vero della pagina.

Esempio:

```html
<html>
  <h1>Hello</h1>
</html>
```

Con il metodo `HEAD`, il server restituisce solo gli header e non il body.

---

# 🚀 Test effettuato

## Avvio script

```bash
python3 banner-grabber.py
```

---

# 📌 Output atteso

Esempio di output possibile:

```text
HTTP/1.1 200 OK
Date: ...
Server: ...
Content-Type: text/html
Content-Length: ...
```

---

# 📌 Cosa è stato imparato

- creazione di una socket in Python
- connessione a un servizio remoto
- invio di una richiesta HTTP manuale
- ricezione degli header HTTP
- differenza tra header e body
- utilizzo di `.encode()` e `.decode()`
- utilizzo di `settimeout()`
- concetto di banner grabbing

---

# 📸 Screenshot



---

# 📚 Utilizzo pratico

Il banner grabbing è utile in:

- cybersecurity
- network analysis
- reconnaissance
- vulnerability assessment
- troubleshooting
- penetration testing

---

# ⚠️ Disclaimer

Questo laboratorio è stato svolto esclusivamente in un ambiente controllato e per scopi educativi.
