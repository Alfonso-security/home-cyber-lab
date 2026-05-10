# Nmap Basics

## Obiettivo

Utilizzare Nmap per eseguire una scansione di rete base e comprendere il funzionamento delle porte, dei servizi e dell’enumeration in cybersecurity.

---

# Cos’è Nmap

Nmap, abbreviazione di Network Mapper, è uno strumento utilizzato per analizzare host e reti.

Permette di:

- identificare host raggiungibili
- rilevare porte aperte
- individuare servizi attivi
- raccogliere informazioni di rete
- eseguire attività di enumeration

Nmap è uno degli strumenti più utilizzati in cybersecurity, penetration testing e network analysis.

---

# Concetti fondamentali

## Host

Un host è un dispositivo collegato a una rete.

Esempi:

- computer
- server
- router
- macchina virtuale

  
## Spiegazione del comando

nmap → avvia il tool Nmap
scanme.nmap.org → host di destinazione autorizzato per test pubblici

## Output analizzato

PORT     STATE  SERVICE

22/tcp   open   ssh

80/tcp   open   http

443/tcp  open   https

##Spiegazione output

PORT → indica numero di porta e protocollo

STATE → indica lo stato della porta

SERVICE → indica il servizio associato alla porta

##Stati principali

open → la porta è aperta e un servizio risponde

closed → la porta è chiusa

filtered → un firewall o filtro impedisce a Nmap di determinare lo stato
<img width="1275" height="761" alt="Screenshot 2026-05-10 021656" src="https://github.com/user-attachments/assets/ffb5f38c-6fa0-4394-bd89-50f82175ee0b" />

## Concetti appresi

Concetto di host

Concetto di porta

Concetto di servizio

Differenza tra porta aperta, chiusa e filtrata

Prima fase di enumeration


# Nota importante

Usa Nmap solo su:

macchine tue
laboratori
TryHackMe
Hack The Box
scanme.nmap.org
ambienti aziendali autorizzati

Nel laboratorio viene utilizzato:

```text
scanme.nmap.org
