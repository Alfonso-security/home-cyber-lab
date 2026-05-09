# Linux Basic Commands

## Obiettivo

Documentare i principali comandi Linux utilizzati durante il laboratorio personale di cybersecurity.

---

# Navigazione nel filesystem

## pwd
```bash
pwd
```

Mostra il percorso della directory corrente.

Utilizzo

Permette di identificare la posizione attuale all’interno del filesystem Linux.

## ls
```bash
ls
```

Mostra i file e le directory presenti nella cartella corrente.

Utilizzo

Permette di visualizzare il contenuto di una directory.

## cd
```bash
cd Desktop
```
Permette di cambiare directory.

Utilizzo

Serve per navigare tra le cartelle del filesystem Linux.

Gestione file e directory

## mkdir
```bash
mkdir test
```
Crea una nuova directory.

Utilizzo

Serve per creare cartelle all’interno del filesystem.

## touch
```bash
touch file.txt
```
Crea un nuovo file vuoto.

Utilizzo

Utile per creare rapidamente file di testo o file di configurazione.

## cp
```bash
cp file.txt copia.txt
```
Copia un file da una posizione a un’altra.

Utilizzo

Permette di duplicare file o directory.

## mv
```bash
mv file.txt document.txt
```
Sposta o rinomina file e directory.

Utilizzo

Può essere utilizzato per organizzare o rinominare elementi del filesystem.

## rm
```bash
rm file.txt
```
Elimina un file.

Utilizzo

Serve per rimuovere file non necessari dal sistema.

Visualizzazione contenuto file
## cat
```bash
cat file.txt
```
Mostra il contenuto di un file nel terminale.

Utilizzo

Utile per leggere rapidamente file di testo.

Networking base
## ip a
```bash
ip a
```
Mostra le interfacce di rete e gli indirizzi IP assegnati.

Utilizzo

Permette di verificare la configurazione della rete locale.

## ping
```bash
ping google.com
```
Verifica la connessione verso un host remoto.

Utilizzo

Serve per controllare la connettività internet e il tempo di risposta della rete.

Aggiornamento sistema
```bash
sudo apt update && sudo apt upgrade -y
```
Aggiorna il sistema operativo e i pacchetti installati.

# Linux Users & Permissions

## whoami
```bash
whoami
```
Mostra l’utente attualmente loggato nel sistema.

Utilizzo

Permette di identificare quale account sta eseguendo i comandi nel terminale.

## groups
```bash
groups
```
Mostra i gruppi associati all’utente corrente.

Utilizzo

Permette di verificare i gruppi e i privilegi associati all’account utilizzato

##sudo
```bash
sudo apt update
```
Permette di eseguire un comando con privilegi amministrativi.

Significato
```bash
superuser do
```
Utilizzo

Utilizzato per eseguire operazioni che richiedono privilegi elevati, come aggiornamenti di sistema o installazione software.


## Root User
```bash
root
```
L’utente root rappresenta l’amministratore del sistema Linux.

L’utente root può:

leggere qualsiasi file
modificare configurazioni di sistema
installare software
gestire utenti e gruppi
controllare completamente il sistema operativo

## Permessi Linux
```bash
ls -l
ls -l
```
Mostra file e directory in formato dettagliato.

Esempio output
```
-rwxr-xr-x
```
>
| Sezione        | Significato  |
| -------------- | ------------ |
| primo blocco   | proprietario |
| secondo blocco | gruppo       |
| terzo blocco   | altri utenti |

>
| Lettera | Significato |
| ------- | ----------- |
| r       | read        |
| w       | write       |
| x       | execute     |

## chmod
```bash
chmod +x
chmod +x script.sh
```
Aggiunge il permesso di esecuzione a un file.

Significato
change mode
Utilizzo

Permette di rendere eseguibili script Bash o altri file eseguibili.
<img width="1278" height="767" alt="Screenshot 2026-05-10 004313" src="https://github.com/user-attachments/assets/ec7e656c-2dd1-4639-ae09-e6bfab3b61a8" />
Script Bash
Creazione script
```bash
nano script.sh

#!/bin/bash

echo "Cybersecurity Lab"
```
## Esecuzione script
./script.sh

Significato
```bash
./
```
Indica di eseguire il file presente nella directory corrente.

## Concetti appresi
utenti Linux

gruppi Linux

permessi file

execute bit

privilegi amministrativi

root user

shell scripting base

gestione sicurezza file



