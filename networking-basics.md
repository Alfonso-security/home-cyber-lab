# Networking Basics

## Obiettivo

Documentare i concetti base di networking studiati nel laboratorio Kali Linux.

---

## Indirizzo IP

Un indirizzo IP identifica un dispositivo all’interno di una rete.

Esempio:

```text
10.0.2.15
```
Nel mio laboratorio, l’indirizzo 10.0.2.15 rappresenta l’IP locale della macchina virtuale Kali Linux in VirtualBox con rete NAT.

## Localhost
127.0.0.1

```127.0.0.1 ``` rappresenta il computer stesso.

Viene usato per testare servizi locali senza uscire su internet.

## Comandi utilizzati
Visualizzare le interfacce di rete
```Bash
ip a
```
Mostra le interfacce di rete e gli indirizzi IP assegnati.

Visualizzare il nome della macchina
```Bash
hostname
```
Testare la connessione
```Bash
ping google.com
```
Verifica la connettività verso un host remoto.

Testare localhost
```Bash
ping 127.0.0.1
```
Verifica che lo stack di rete locale funzioni correttamente.

## Concetti appresi
indirizzo IP

rete locale

localhost

interfacce di rete

connettività

host
