# Linux Process Management

## Obiettivo

Comprendere il funzionamento dei processi Linux e la gestione di foreground, background e monitoraggio processi.

---

# Cos’è un processo

Un processo è un programma in esecuzione nel sistema operativo.

Esempi:
- browser
- terminale
- nano
- python
- server web

---

# PID

Ogni processo possiede un identificatore unico chiamato:

```text
PID = Process ID
```
Il PID permette di:

identificare processi

monitorare processi

terminare processi

## Visualizzare processi
Comando base

```Bash
ps
```
Mostra i processi associati al terminale corrente.

## Visualizzare tutti i processi

```Bash
ps aux
```
Significato opzioni

| Opzione | Significato                      |
| ------- | -------------------------------- |
| a       | processi di tutti gli utenti     |
| u       | formato dettagliato              |
| x       | include processi senza terminale |

## Output esempio
```text
USER       PID %CPU %MEM COMMAND
root         1  0.0  0.1 /sbin/init
kali      2200  1.2  2.1 firefox
```
## Cercare processi
grep
```Bash
ps aux | grep nano
```
Permette di filtrare l’output dei processi cercando una parola specifica.

Pipe
```Bash
|
```
La pipe prende l’output di un comando e lo passa al comando successivo.
## Esempio
```Bash
ps aux | grep python
```
Mostra solo i processi contenenti la parola python.
<img width="1279" height="761" alt="Screenshot 2026-05-10 011130" src="https://github.com/user-attachments/assets/5c39fcbd-7bf8-4017-b408-99b85e556a8f" />

Terminare processi
kill
```Bash
kill PID
```
Termina un processo utilizzando il suo Process ID.

Esempio
```Bash
kill 2200
```
Terminazione forzata
```Bash
kill -9 PID
```
Forza la chiusura immediata del processo.

## Monitoraggio processi live
top
```Bash
top
```
Mostra:

CPU

RAM

processi attivi

utilizzo risorse

## Uscire da top
```Bash
q
```
# Foreground Process

Un processo in foreground:

occupa il terminale

blocca Bash finché non termina

## Esempio
```Bash
sleep 60
```
Il terminale resta occupato per 60 secondi.

## Background Process
Un processo in background:

continua a funzionare

lascia il terminale utilizzabile

## Avvio background
```Bash
sleep 60 &
```
Simbolo &
```Bash
&
```
Indica:
```text
esegui processo in background
```
Visualizzare processi background
```Bash
jobs
```
Mostra i job attivi in background.

Portare job foreground
```Bash
fg
```
Riporta il job in foreground.

Mandare job background
```Bash
bg
```
Invia un job sospeso in background.

Interrompere un processo
```text
CTRL + C
```
Interrompe il processo attualmente in esecuzione.

Sospendere un processo
```text
CTRL + Z
```
Sospende temporaneamente il processo corrente.

## Editor Nano

Aprire file
```Bash
nano file.txt
```
Funzionamento

Nano permette di:

creare file

modificare file

scrivere script Bash

Salvare in Nano
```text
CTRL + O
```
Uscire da Nano
```text
CTRL + X
```
# Script Bash
Creazione script
```Bash
nano script.sh
```
Esempio scrip
```Bash
#!/bin/bash

echo "Cybersecurity Lab"
```
## Rendere eseguibile

```Bash
chmod +x script.sh
```
Eseguire script
```Bash
./script.sh
```
Significato ./
```text
esegui file presente nella directory corrente
```
Permessi Linux

Visualizzare permessi
```Bash
ls -l
```
## Esempio output
```text
-rwxr-xr-x
```
| Parte           | Significato  |
| --------------- | ------------ |
| primo carattere | tipo file    |
| primo blocco    | owner        |
| secondo blocco  | gruppo       |
| terzo blocco    | altri utenti |

## Significato lettere
| Lettera | Significato |
| ------- | ----------- |
| r       | read        |
| w       | write       |
| x       | execute     |

## chmod
```Bash
chmod +x script.sh
```
Aggiunge il permesso execute.

Utenti Linux

## Utente corrente
```Bash
whoami
```
## Gruppi utente
```Bash
groups
```
Mostra i gruppi associati all’utente corrente.

## sudo
```Bash
sudo apt update
```
Permette di eseguire comandi con privilegi amministrativi.

## root

L’utente root possiede il controllo completo del sistema Linux.

Concetti appresi

processi Linux

PID

foreground/background

ps

grep

kill

top

jobs

Bash scripting

Nano

permessi Linux

utenti e gruppi

sudo

root
