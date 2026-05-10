# 🖥️ tcpdump Basics

Questo documento contiene analisi pratiche del traffico di rete effettuate con tcpdump all’interno di Kali Linux.

A differenza di Wireshark, tcpdump funziona completamente da terminale (CLI) ed è molto utilizzato in:
- Linux administration
- troubleshooting rete
- cybersecurity
- server remoti
- SOC analysis

---

# 🖥️ Ambiente di laboratorio

| Componente | Dettagli |
|---|---|
| Sistema Operativo | Kali Linux |
| Virtualizzazione | VirtualBox |
| Interfaccia di rete | eth0 |
| Tool utilizzato | tcpdump |

---

# 📡 Introduzione a tcpdump

tcpdump è uno strumento da terminale utilizzato per:
- catturare pacchetti
- analizzare traffico rete
- filtrare protocolli
- monitorare connessioni

È considerato uno dei tool fondamentali nel networking Linux.

---

# 🔍 Verifica installazione

## Comando utilizzato

```bash
which tcpdump
```

---

## Spiegazione comando

| Parte | Significato |
|---|---|
| which | cerca percorso comando |
| tcpdump | programma cercato |

---

## Cosa sta succedendo

Il sistema controlla se tcpdump è installato e mostra il percorso del programma.

Esempio:

```text
/usr/sbin/tcpdump
```

---

# 🌐 Live Packet Capture

Questa è una cattura live del traffico di rete.

---

## Comando utilizzato

```bash
sudo tcpdump -i eth0
```

---

## Spiegazione comando

| Parte | Significato |
|---|---|
| sudo | esegue come amministratore |
| tcpdump | packet sniffer |
| -i | specifica interfaccia |
| eth0 | scheda rete analizzata |

---

## Cosa sta succedendo

tcpdump:
- ascolta traffico rete
- cattura pacchetti live
- mostra informazioni direttamente nel terminale

---

## Cosa è stato osservato

- traffico DNS
- traffico ICMP
- traffico ARP
- richieste reverse DNS
- traffico TCP/UDP

---

## Screenshot

<img width="1275" height="770" alt="Screenshot 2026-05-10 120844" src="https://github.com/user-attachments/assets/788126ec-67f5-453a-8cb1-27609b8c43ef" />

---

# 📡 ICMP Packet Capture

ICMP viene utilizzato per diagnostica rete.

Il comando più comune è:

```bash
ping
```

---

## Comando utilizzato

```bash
sudo tcpdump -i eth0 icmp
```

---

## Spiegazione comando

| Parte | Significato |
|---|---|
| sudo | privilegi amministratore |
| tcpdump | packet capture |
| -i eth0 | usa interfaccia eth0 |
| icmp | filtra solo traffico ICMP |

---

## Altro comando utilizzato

```bash
ping google.com
```

---

## Cosa sta succedendo

tcpdump mostra:
- Echo Request
- Echo Reply

generati dal comando ping.

---

## Cosa è stato osservato

- richieste ICMP
- risposte ICMP
- indirizzi IP sorgente/destinazione
- pacchetti live

---

# 🌐 DNS Packet Capture

DNS traduce domini in indirizzi IP.

---

## Comando utilizzato

```bash
sudo tcpdump -i eth0 port 53
```

---

## Spiegazione comando

| Parte | Significato |
|---|---|
| sudo | privilegi amministratore |
| tcpdump | packet sniffer |
| -i eth0 | interfaccia rete |
| port 53 | filtra traffico DNS |

---

## Cosa sta succedendo

tcpdump mostra solamente:
- query DNS
- risposte DNS

sulla porta 53.

---

## Cosa è stato osservato

- richieste DNS
- traffico UDP
- risposte DNS
- nomi dominio

---

## Screenshot

<img width="1273" height="764" alt="Screenshot 2026-05-10 121153" src="https://github.com/user-attachments/assets/e83d3c62-32b5-43db-83c2-e1d392da17ed" />

---

# 🔐 HTTPS Packet Capture

HTTPS utilizza TLS per cifrare il traffico web.

---

## Comando utilizzato

```bash
sudo tcpdump -i eth0 port 443
```

---

## Spiegazione comando

| Parte | Significato |
|---|---|
| sudo | privilegi amministratore |
| tcpdump | packet capture |
| -i eth0 | interfaccia rete |
| port 443 | traffico HTTPS |

---

## Cosa sta succedendo

tcpdump cattura traffico HTTPS/TLS.

Il contenuto:
- NON è leggibile
- è cifrato

---

## Cosa è stato osservato

- traffico TLS
- connessioni HTTPS
- pacchetti cifrati

---

# 🌍 HTTP Packet Capture

HTTP è traffico web non cifrato.

---

## Comando utilizzato

```bash
sudo tcpdump -i eth0 port 80
```

---

## Spiegazione comando

| Parte | Significato |
|---|---|
| sudo | privilegi amministratore |
| tcpdump | packet capture |
| -i eth0 | interfaccia rete |
| port 80 | traffico HTTP |

---

## Cosa sta succedendo

tcpdump cattura traffico HTTP non cifrato.

---

## Cosa è stato osservato

- traffico web HTTP
- connessioni TCP
- pacchetti leggibili

---

# 🛑 Terminare la cattura

## Combinazione utilizzata

```text
CTRL + C
```

---

## Cosa sta succedendo

tcpdump interrompe la cattura e mostra:
- pacchetti catturati
- pacchetti ricevuti
- eventuali pacchetti persi

---

#  Competenze praticate

- packet capture da terminale
- analisi traffico rete
- filtering protocolli
- traffico DNS
- traffico ICMP
- traffico HTTP/HTTPS
- troubleshooting rete
- utilizzo tcpdump
- networking Linux

---

#  Differenza Wireshark vs tcpdump

| Tool | Tipo |
|---|---|
| Wireshark | GUI (grafico) |
| tcpdump | CLI (terminale) |

---

## Wireshark

Più comodo per:
- analisi dettagliata
- visualizzazione pacchetti
- protocol inspection

---

## tcpdump

Più usato per:
- server Linux
- SSH remoto
- troubleshooting rapido
- ambienti senza GUI

---

# ⚠️ Disclaimer

Tutte le analisi del traffico sono state effettuate all’interno di un laboratorio personale controllato esclusivamente per scopi educativi.
