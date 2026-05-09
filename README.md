# Home Cyber Lab 🛡️

Repository personale creato per documentare il mio percorso pratico nello studio della cybersecurity.

L'obiettivo del progetto è costruire un laboratorio domestico sicuro e controllato dove esercitarmi con Linux, networking, scansione delle porte, analisi dei servizi e strumenti base di sicurezza informatica.

---

## Obiettivo del progetto

Questo laboratorio nasce per:

- imparare a usare Linux in ambito cybersecurity;
- comprendere le basi del networking;
- analizzare porte, servizi e connessioni attive;
- usare strumenti come Nmap in modo corretto ed etico;
- documentare il mio percorso di apprendimento;
- costruire un portfolio tecnico da mostrare ad aziende e recruiter.

---

## Ambiente di laboratorio

Il laboratorio è configurato in ambiente virtualizzato.

| Componente | Dettaglio |
|---|---|
| Host OS | Windows |
| Virtualizzazione | VirtualBox |
| Sistema operativo VM | Kali Linux |
| RAM VM | 4 GB |
| CPU VM | 2 vCPU |
| Disco VM | 40 GB |
| Rete | NAT / ambiente controllato |

---

## Argomenti documentati

| File | Descrizione |
|---|---|
| [kali-setup.md](./kali-setup.md) | Installazione e configurazione base di Kali Linux |
| [linux-commands.md](./linux-commands.md) | Comandi Linux fondamentali per muoversi nel terminale |
| [linux-process-management.md](./linux-process-management.md)| Gestione processi Linux e Bash |
| [networking-basics.md](./networking-basics.md) | Concetti base di networking |
| [tcp-udp.md](./tcp-udp.md) | Differenze tra TCP e UDP |
| [http-https.md](./http-https.md) | Differenze tra HTTP e HTTPS |
| [listening-ports.md](./listening-ports.md) | Analisi delle porte in ascolto e delle connessioni attive |
| [nmap-basics.md](./nmap-basics.md) | Utilizzo base di Nmap per scansioni autorizzate |

---

## Competenze sviluppate

Durante questo percorso sto sviluppando competenze pratiche su:

- gestione base di una distribuzione Linux;
- utilizzo della shell Bash;
- aggiornamento e gestione dei pacchetti;
- navigazione del file system;
- gestione di processi e servizi;
- concetti di IP, porte, protocolli e connessioni;
- differenza tra TCP e UDP;
- analisi delle porte aperte;
- utilizzo base di Nmap;
- lettura e interpretazione degli output da terminale;
- documentazione tecnica in Markdown.

## Esempi di comandi studiati

```bash
sudo apt update && sudo apt upgrade -y
```
Aggiorna la lista dei pacchetti disponibili e installa gli aggiornamenti del sistema.
```bash
ip a
```
Mostra le interfacce di rete e gli indirizzi IP assegnati alla macchina.
```bash
ping google.com
```
Verifica la connettività verso un host remoto.
```bash
ss -tuln
```
Mostra le porte TCP e UDP in ascolto sul sistema.
```bash
ss -tanp
```
Mostra le connessioni TCP attive, il loro stato e i processi associati.
```bash
nmap scanme.nmap.org
```
Esegue una scansione base su un target autorizzato.
# Stato del progetto
| Modulo                   | Stato            |
| ------------------------ | ---------------- |
| Setup Kali Linux         | ✅ Completato     |
| Comandi Linux base       | ✅ Completato     |
| Networking base          | ✅ Completato     |
| TCP / UDP                | ✅ Completato     |
| HTTP / HTTPS             | ✅ Completato     |
| Listening ports          | ✅ Completato     |
| Nmap base                | ✅ Completato     |
| Wireshark                | 🔄 Da aggiungere |
| TryHackMe labs           | 🔄 Da aggiungere |
| Bash scripting           | 🔄 Da aggiungere |
| Python for cybersecurity | 🔄 Da aggiungere |

## Regole etiche

Tutti i comandi, gli strumenti e gli esempi presenti in questo repository sono usati esclusivamente in:

ambienti personali;
macchine virtuali controllate;
piattaforme autorizzate come TryHackMe o Hack The Box;
target pubblici espressamente autorizzati, come scanme.nmap.org.

Questo repository non ha finalità offensive.
Lo scopo è esclusivamente formativo e professionale.

## Prossimi obiettivi

I prossimi argomenti che intendo aggiungere sono:

analisi del traffico con Wireshark;
esercizi pratici su TryHackMe;
script Bash di base;
introduzione a Python per la cybersecurity;
gestione utenti, gruppi e permessi Linux;
hardening base di una macchina Linux;
report tecnici dei laboratori svolti.
## Profilo

Sono uno studente magistrale in cybersecurity e sto costruendo questo repository come portfolio pratico per documentare il mio percorso di crescita tecnica.

Il progetto verrà aggiornato progressivamente con nuovi appunti, esercizi, comandi, screenshot e report di laboratorio.

## Note

Questo repository rappresenta un percorso di apprendimento continuo.
Ogni file viene scritto con l'obiettivo di spiegare non solo il comando utilizzato, ma anche il motivo per cui viene usato e cosa significa il suo output.
