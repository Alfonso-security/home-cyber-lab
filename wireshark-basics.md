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

![DNS Analysis](screenshots/wireshark/wireshark-dns-ipv4-ipv6-analysis.png)

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

![TCP Handshake](screenshots/wireshark/wireshark-tcp-handshake-analysis.png)

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

![TLS Analysis](screenshots/wireshark/wireshark-tls-encrypted-traffic-analysis.png)

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

![HTTP Analysis](screenshots/wireshark/wireshark-http-get-request-analysis.png)

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

![ICMP Analysis](screenshots/wireshark/wireshark-icmp-echo-request-reply-analysis.png)

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

![ARP Analysis](screenshots/wireshark/wireshark-arp-resolution-analysis.png)

---

# 📸 Struttura screenshots

```text
screenshots/
└── wireshark/
    ├── wireshark-dns-ipv4-ipv6-analysis.png
    ├── wireshark-tcp-handshake-analysis.png
    ├── wireshark-http-get-request-analysis.png
    ├── wireshark-tls-encrypted-traffic-analysis.png
    ├── wireshark-icmp-echo-request-reply-analysis.png
    └── wireshark-arp-resolution-analysis.png
```

---

# 🚀 Competenze praticate

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

# ⚠️ Disclaimer

Tutte le analisi sono state effettuate all’interno di un laboratorio personale controllato esclusivamente per scopi educativi.
