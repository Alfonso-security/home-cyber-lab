# HTTP and HTTPS Basics

## Obiettivo

Comprendere il funzionamento delle comunicazioni web e della cifratura HTTPS.

---

# HTTP

HTTP significa:

```text
HyperText Transfer Protocol
```
È il protocollo utilizzato dai browser per comunicare con i server web.

Porta HTTP
```text
80/TCP
```
## Problema HTTP

HTTP non cifra i dati.

Questo significa che:

password

cookie

dati sensibili

potrebbero essere intercettati.

## HTTPS

HTTPS significa:
```text
HyperText Transfer Protocol Secure
```
HTTPS utilizza TLS per cifrare la comunicazione.

Porta HTTPS
```text
443/TCP
```
## TLS
TLS significa:
```text
Transport Layer Security
```
Garantisce:

cifratura

integrità dati

autenticazione server

## Certificati digitali
HTTPS utilizza certificati digitali per verificare l’identità del server.

Il browser controlla:

validità certificato

dominio corretto

Certificate Authority trusted

## Flusso comunicazione HTTPS
```text
Browser
↓
DNS lookup
↓
TCP Handshake
↓
TLS Handshake
↓
Connessione cifrata
↓
HTTP Request
↓
HTTP Response
```
##DNS Lookup

Il browser converte:
```text
google.com
```
in un indirizzo IP.

## TCP Handshake
```text
Client → SYN
Server → SYN-ACK
Client → ACK
```
## TLS Handshake

Client e server:

verificano certificato

negoziano cifratura

generano chiavi crittografiche


HTTP Request
Esempio:
```text
GET /
```
Richiede la pagina principale del sito.

HTTP Response

Il server restituisce:

HTML

CSS

JavaScript

immagini

# Status Code HTTP

| Codice | Significato           |
| ------ | --------------------- |
| 200    | OK                    |
| 301    | Redirect              |
| 403    | Forbidden             |
| 404    | Not Found             |
| 500    | Internal Server Error |

# Comandi utilizzati

Richiesta web semplice
```Bash
curl https://example.com
```
Visualizzare solo gli header
```Bash
curl -I https://google.com
```
curl-http-headers.png
<img width="1271" height="760" alt="Screenshot 2026-05-10 014009" src="https://github.com/user-attachments/assets/0b6e5fbe-1cd5-4167-b933-9bf73c3aa331" />


Modalità verbose
```Bash
curl -v https://google.com
```
curl-verbose-https.png
<img width="1267" height="761" alt="Screenshot 2026-05-10 012921" src="https://github.com/user-attachments/assets/1205df6c-df73-4928-bb67-5a6ff944bef6" />
Mostra:

DNS

TCP

TLS

HTTP

# Cookie
I server possono inviare:
```text
Set-Cookie
```
I cookie vengono salvati dal browser per:

login

sessioni

autenticazione

# Concetti di cybersecurity appresi
HTTP

HTTPS

TLS

cifratura

certificati digitali

header HTTP

cookie

status code

traffico web
