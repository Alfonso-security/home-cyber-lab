# TCP and UDP Basics

## Obiettivo

Comprendere la differenza tra TCP e UDP e il loro ruolo nella comunicazione di rete.

---

## TCP

TCP significa:

```text
Transmission Control Protocol
```
## TCP è un protocollo orientato alla connessione.

Garantisce:

affidabilità

ordine dei dati

controllo errori

ritrasmissione dei pacchetti persi

## Three-Way Handshake

Prima di comunicare, TCP stabilisce una connessione tramite handshake.
```text
Client → SYN
Server → SYN-ACK
Client → ACK
```
Dopo questi passaggi, la connessione diventa:
```text
ESTABLISHED
```
## Significato degli acronimi
```text
SYN → Synchronize
ACK → Acknowledgement
SYN-ACK → conferma e sincronizzazione
```
## UDP
UDP significa:
```text
User Datagram Protocol
```
UDP è più veloce di TCP, ma non garantisce che i dati arrivino
Non usa handshake.

È usato quando la velocità è più importante dell’affidabilità

## Differenza TCP/UDP

| Caratteristica   | TCP              | UDP                  |
| ---------------- | ---------------- | -------------------- |
| Connessione      | Sì               | No                   |
| Affidabilità     | Alta             | Bassa                |
| Velocità         | Più lento        | Più veloce           |
| Controllo errori | Sì               | No                   |
| Esempi           | HTTP, HTTPS, SSH | DNS, VoIP, streaming |

## Comandi utilizzati

Visualizzare connessioni TCP
```Bash
ss -t
```
Visualizzare connessioni UDP
```Bash
ss -u
```
Visualizzare connessioni TCP attive

```Bash
ss -tan
```
## Stati TCP principali

| Stato       | Significato                                          |
| ----------- | ---------------------------------------------------- |
| LISTEN      | il servizio aspetta connessioni                      |
| ESTABLISHED | connessione attiva                                   |
| TIME_WAIT   | connessione chiusa ma ancora in attesa               |
| CLOSE_WAIT  | il peer ha chiuso, ma il programma locale non ancora |
| SYN_SENT    | tentativo di connessione in corso                    |
| SYN_RECV    | SYN ricevuto, handshake non ancora completato        |

## Concetti appresi
TCP

UDP

handshake

SYN

ACK

ESTABLISHED

stati TCP
