# 🦈 Wireshark Basics

Questo documento contiene analisi pratiche del traffico di rete effettuate con Wireshark all’interno di una macchina virtuale Kali Linux.

L’obiettivo è comprendere il funzionamento dei principali protocolli di rete attraverso l’analisi di traffico reale.

---

# 🖥️ Ambiente di laboratorio

| Componente | Dettagli |
|---|---|
| Sistema Operativo | Kali Linux |
| Virtualizzazione | VirtualBox |
| Interfaccia di rete | eth0 |
| Tool utilizzato | Wireshark |

---

# 🌐 DNS Analysis

DNS (Domain Name System) serve a tradurre i nomi dei domini in indirizzi IP.

Esempio:

```text
google.com → 172.x.x.x
```

Senza DNS dovremmo ricordare direttamente gli indirizzi IP dei siti web.

---

## Filtro utilizzato

```text
dns
```

### Spiegazione

Questo filtro mostra solamente il traffico DNS.

Serve a visualizzare:
- richieste DNS
- risposte DNS
- traduzione dominio → IP

---

## Comandi utilizzati

```bash
nslookup google.com
```

### Spiegazione comando

| Parte | Significato |
|---|---|
| nslookup | tool per interrogare server DNS |
| google.com | dominio da risolvere |

### Cosa sta succedendo

La macchina chiede al server DNS:

```text
Qual è l’indirizzo IP di google.com?
```

---

```bash
ping google.com
```

### Spiegazione comando

| Parte | Significato |
|---|---|
| ping | invia pacchetti ICMP |
| google.com | destinazione |

### Cosa sta succedendo

Prima viene effettuata una richiesta DNS per ottenere l’IP del dominio.

Successivamente vengono inviati pacchetti ICMP verso quell’indirizzo IP.

---

## Cosa è stato osservato

- richieste DNS
- risposte DNS
- traffico UDP porta 53
- record IPv4 e IPv6

---

## Screenshot

<img width="1276" height="758" alt="Screenshot 2026-05-10 115117" src="https://github.com/user-attachments/assets/94f4129d-a273-4ab2-9fce-9961df803a5b" />

---

# 🤝 TCP Three-Way Handshake

TCP utilizza un processo in tre fasi per aprire una connessione affidabile.

---

## Filtro utilizzato

```text
tcp
```

### Spiegazione

Mostra solamente pacchetti TCP.

Serve ad analizzare:
- connessioni
- handshake
- ACK
- FIN
- RST

---

## Comando utilizzato

```bash
curl http://example.com
```

### Spiegazione comando

| Parte | Significato |
|---|---|
| curl | tool per effettuare richieste web |
| http:// | protocollo HTTP |
| example.com | sito richiesto |

### Cosa sta succedendo

Il sistema:
1. apre connessione TCP
2. esegue handshake TCP
3. invia richiesta HTTP GET

---

## Fasi Handshake TCP

| Pacchetto | Significato |
|---|---|
| SYN | richiesta connessione |
| SYN-ACK | server accetta |
| ACK | connessione confermata |

---

## Cosa è stato osservato

- SYN
- SYN ACK
- ACK
- apertura connessione TCP

---

## Screenshot

<img width="1269" height="763" alt="Screenshot 2026-05-10 105605" src="https://github.com/user-attachments/assets/4874adde-4acd-4a30-ac35-d41f8a8df15c" />

---

# 🔐 TLS / HTTPS Analysis

TLS cifra la comunicazione di rete.

HTTPS utilizza TLS per proteggere il traffico web.

---

## Filtro utilizzato

```text
tls
```

### Spiegazione

Mostra solamente traffico TLS/HTTPS.

Serve per visualizzare:
- Client Hello
- Server Hello
- traffico cifrato

---

## Comando utilizzato

```bash
curl https://google.com
```

### Spiegazione comando

| Parte | Significato |
|---|---|
| curl | richiesta web |
| https:// | protocollo HTTPS cifrato |
| google.com | server remoto |

### Cosa sta succedendo

Il sistema:
1. apre connessione TCP
2. avvia handshake TLS
3. cifra comunicazione

---

## Cosa è stato osservato

- Client Hello
- Server Hello
- TLSv1.3
- traffico cifrato

---

## Concetto importante

Con HTTP:
- il traffico è leggibile

Con HTTPS:
- il traffico è cifrato

---

## Screenshot

<img width="1269" height="752" alt="Screenshot 2026-05-10 114403" src="https://github.com/user-attachments/assets/161a2273-3c80-482a-92af-480a7510aefd" />

---

# 🌍 HTTP Analysis

HTTP è un protocollo web non cifrato.

---

## Filtro utilizzato

```text
http
```

### Spiegazione

Mostra solamente traffico HTTP.

Permette di leggere:
- richieste GET
- header
- risposte server

---

## Comando utilizzato

```bash
curl http://example.com
```

### Spiegazione comando

| Parte | Significato |
|---|---|
| curl | client web da terminale |
| http:// | protocollo non cifrato |
| example.com | server remoto |

### Cosa sta succedendo

La macchina:
1. apre connessione TCP
2. invia richiesta HTTP GET
3. riceve risposta server

---

## Cosa è stato osservato

- GET request
- 200 OK
- Host
- User-Agent
- header HTTP

---

## Screenshot

<img width="1273" height="764" alt="Screenshot 2026-05-10 111502" src="https://github.com/user-attachments/assets/36d9bbdc-289f-4035-a73d-af9d29e3bbfc" />

---

# 📡 ICMP Analysis

ICMP viene utilizzato per diagnostica di rete.

Il comando più comune è:

```bash
ping
```

---

## Filtro utilizzato

```text
icmp
```

### Spiegazione

Mostra solamente traffico ICMP.

Serve per visualizzare:
- Echo Request
- Echo Reply

---

## Comando utilizzato

```bash
ping google.com
```

### Spiegazione comando

| Parte | Significato |
|---|---|
| ping | invia richieste ICMP |
| google.com | destinazione |

### Cosa sta succedendo

La macchina:
1. risolve il dominio tramite DNS
2. invia Echo Request
3. riceve Echo Reply

---

## Cosa è stato osservato

- Echo Request
- Echo Reply
- TTL
- sequence number

---

## Concetti importanti

| Campo | Significato |
|---|---|
| TTL | numero massimo di salti rete |
| seq | ordine pacchetti |
| Echo Request | richiesta ping |
| Echo Reply | risposta ping |

---

## Screenshot

<img width="1272" height="763" alt="Screenshot 2026-05-10 120252" src="https://github.com/user-attachments/assets/8efcc426-f393-4f87-9d99-f3d39563f03d" />

---

# 🖧 ARP Analysis

ARP converte indirizzi IP in indirizzi MAC nella rete locale.

---

## Filtro utilizzato

```text
arp
```

### Spiegazione

Mostra solamente traffico ARP.

Serve per visualizzare:
- richieste MAC
- risposte MAC

---

## Comando utilizzato

```bash
arp -a
```

### Spiegazione comando

| Parte | Significato |
|---|---|
| arp | visualizza cache ARP |
| -a | mostra tutti gli indirizzi |

### Cosa sta succedendo

Il sistema mostra:
- associazioni IP ↔ MAC
- dispositivi rete locale

---

## Altro comando utilizzato

```bash
ping 10.0.2.2
```

### Cosa sta succedendo

Prima del ping:
- il sistema deve conoscere il MAC del destinatario
- viene quindi effettuata richiesta ARP

---

## Cosa è stato osservato

- richieste ARP
- risposte ARP
- risoluzione MAC address

---

## Screenshot

<img width="1269" height="760" alt="Screenshot 2026-05-10 122023" src="https://github.com/user-attachments/assets/8cae534d-dd57-446a-9e22-ede86345747c" />


---

#  Competenze praticate

- packet capture
- filtraggio traffico
- troubleshooting rete
- analisi DNS
- analisi TCP
- analisi TLS
- analisi HTTP
- diagnostica ICMP
- risoluzione ARP
- interpretazione protocolli
- utilizzo filtri Wireshark

---
# 🚨 Suspicious TCP Reset Analysis

Questa analisi mostra pacchetti TCP Reset (RST) generati durante una scansione Nmap.

---

## Filtro utilizzato

```text
tcp.flags.reset == 1
```

---

## Comando utilizzato

```bash
nmap scanme.nmap.org
```

---

## Spiegazione

Durante una scansione Nmap:
- il client invia richieste SYN
- il server può rispondere con RST
- questo indica porte chiuse o connessioni rifiutate

---

## Cosa è stato osservato

- TCP SYN packets
- TCP RST packets
- closed ports
- scan behavior
- abnormal connection attempts

---

## Concetti importanti

| Flag | Significato |
|---|---|
| SYN | richiesta connessione |
| ACK | conferma |
| RST | reset connessione |

RST viene spesso utilizzato per:
- rifiutare connessioni
- indicare porte chiuse
- terminare sessioni TCP

---

## Screenshot

<img width="1280" height="767" alt="Screenshot 2026-05-10 171204" src="https://github.com/user-attachments/assets/a604d71a-88ad-4d1c-94d4-f9293801b659" />

# 🛰️ Local TCP Communication with Netcat

Questa analisi mostra una comunicazione TCP locale effettuata tramite Netcat sulla porta 4444.

---

## Filtro utilizzato

```text
tcp.port == 4444
```

---

## Comandi utilizzati

Server:

```bash
nc -lvnp 4444
```

Client:

```bash
nc 127.0.0.1 4444
```

---

## Spiegazione

La prima istanza Netcat:
- apre una porta in ascolto

La seconda:
- si connette localmente tramite loopback interface (`lo`)

---

## Cosa è stato osservato

- TCP SYN
- SYN ACK
- ACK
- PSH ACK
- traffico dati TCP
- connessione client/server locale

---

## Concetti importanti

| Campo | Significato |
|---|---|
| SYN | richiesta connessione |
| ACK | conferma |
| PSH | invio dati |
| Loopback (`lo`) | traffico localhost |

---

## Screenshot

<img width="1281" height="762" alt="Screenshot 2026-05-10 173526" src="https://github.com/user-attachments/assets/4c89705a-286b-4cd8-baf5-f1628196ece4" />

# 🔎 Follow TCP Stream Analysis

Questa analisi mostra la ricostruzione completa di una comunicazione TCP tramite la funzione "Follow TCP Stream" di Wireshark.

---

## Funzione utilizzata

```text
Follow → TCP Stream
```

---

## Obiettivo

Ricostruire:
- traffico dati
- payload TCP
- conversazione client/server

---

## Cosa è stato osservato

- stream TCP completo
- traffico Netcat
- dati trasmessi
- payload leggibile

---

## Concetti importanti

Wireshark può:
- ricostruire comunicazioni TCP
- riordinare pacchetti
- mostrare payload applicativo

Questa funzione è molto utilizzata in:
- digital forensics
- SOC analysis
- incident response
- malware analysis

---

## Screenshot

<img width="1270" height="763" alt="Screenshot 2026-05-10 174126" src="https://github.com/user-attachments/assets/f399778c-b990-4b5d-8fb4-205b7bebe6b6" />


# TCP vs UDP Comparison

Durante il laboratorio sono state analizzate comunicazioni TCP e UDP tramite Netcat e Wireshark.

---

## TCP

TCP utilizza:
- handshake
- ACK
- controllo connessione
- affidabilità

Pacchetti osservati:
- SYN
- SYN ACK
- ACK
- PSH
- FIN

---

## UDP

UDP:
- non utilizza handshake
- non utilizza ACK
- invia dati direttamente
- è connectionless

Pacchetti osservati:
- traffico UDP diretto
- payload immediato

---

## Differenze principali

| TCP | UDP |
|---|---|
| affidabile | veloce |
| handshake | no handshake |
| ACK | no ACK |
| connection-oriented | connectionless |
| maggiore overhead | minore overhead |

---

## Screenshot UDP
<img width="1283" height="768" alt="Screenshot 2026-05-11 212444" src="https://github.com/user-attachments/assets/be3e6136-bee5-41e6-903a-8626dd0401ba" />

# 🌍 DNS Query and Response Analysis

Questa analisi mostra richieste e risposte DNS catturate tramite Wireshark.

---

## Filtro utilizzato

```text
dns
```

---

## Comandi utilizzati

```bash
nslookup google.com
```

```bash
nslookup github.com
```

---

## Spiegazione

Il protocollo DNS:
- traduce nomi dominio in indirizzi IP
- permette ai client di raggiungere server Internet

Durante l'analisi sono stati osservati:
- record A (IPv4)
- record AAAA (IPv6)

---

## Cosa è stato osservato

- DNS query
- DNS response
- IPv4 resolution
- IPv6 resolution

---

## Concetti importanti

| Record | Significato |
|---|---|
| A | indirizzo IPv4 |
| AAAA | indirizzo IPv6 |

---

## Screenshot

<img width="1273" height="754" alt="Screenshot 2026-05-11 213948" src="https://github.com/user-attachments/assets/2439c108-1ef4-4bcd-b3b3-6f7852dd4cda" />

# 📊 Network Conversations Analysis

Questa analisi mostra le conversazioni di rete osservate tramite Wireshark.

---

## Funzione utilizzata

```text
Statistics → Conversations
```

---

## Obiettivo

Identificare:
- host sorgente
- host destinazione
- traffico totale
- comunicazioni TCP/UDP

---

## Cosa è stato osservato

- traffico Ethernet
- traffico IPv4
- traffico IPv6
- connessioni TCP
- traffico UDP

---

## Informazioni disponibili

| Campo | Significato |
|---|---|
| Packets | numero pacchetti |
| Bytes | quantità traffico |
| Packets A → B | traffico inviato |
| Packets B → A | traffico ricevuto |

---

## Utilizzo pratico

Questa funzione è molto utilizzata in:
- SOC analysis
- network monitoring
- malware analysis
- troubleshooting
- incident response

---

## Screenshot
<img width="1275" height="761" alt="Screenshot 2026-05-11 215933" src="https://github.com/user-attachments/assets/61ed6523-6f11-4fb3-814c-e23eded32c01" />
# ⚠️ Disclaimer

Tutte le analisi sono state effettuate all’interno di un laboratorio personale controllato esclusivamente per scopi educativi.
