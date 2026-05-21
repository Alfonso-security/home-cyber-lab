# Home Cyber Lab

Personal cybersecurity laboratory built with VirtualBox, Kali Linux and Python.

This repository documents my hands-on learning path in Linux, networking, packet analysis and basic cybersecurity tooling. The goal is to show practical work, clear documentation and steady progress through real lab activities.

## Project Overview

This lab focuses on practical foundations for cybersecurity:

| Area | What I Practiced | Evidence |
|---|---|---|
| Linux | terminal usage, permissions, processes, signals | notes and screenshots |
| Networking | TCP/IP, DNS, HTTP/HTTPS, ICMP, ARP | Wireshark and tcpdump captures |
| Scanning | basic Nmap scans, listening ports, service discovery | scan notes and screenshots |
| Python | sockets, TCP client/server, port scanner, banner grabbing, reverse DNS | scripts and explanations |
| Analysis | packet capture, protocol inspection, troubleshooting | documented lab results |

## Lab Environment

| Component | Details |
|---|---|
| Host OS | Windows |
| Virtualization | VirtualBox |
| Guest OS | Kali Linux |
| RAM | 4 GB |
| CPU | 2 vCPU |
| Network Mode | NAT |
| Main Tools | Wireshark, tcpdump, Netcat, Python, Nmap |

## Repository Structure

| File / Folder | Description |
|---|---|
| [kali-setup.md](kali-setup.md) | Kali Linux installation and virtual machine configuration |
| [linux-commands.md](linux-commands.md) | Essential Linux commands and shell basics |
| [linux-process-management.md](linux-process-management.md) | Linux processes, PID and signal management |
| [networking-basics.md](networking-basics.md) | Core networking concepts |
| [tcp-udp.md](tcp-udp.md) | TCP and UDP fundamentals |
| [listening-ports.md](listening-ports.md) | Listening ports and active network connections |
| [http-https.md](http-https.md) | HTTP, HTTPS and TLS basics |
| [nmap-basics.md](nmap-basics.md) | Introduction to Nmap scanning |
| [wireshark-basics.md](wireshark-basics.md) | Wireshark packet analysis and protocol inspection |
| [tcpdump-basics.md](tcpdump-basics.md) | Packet capture and filtering with tcpdump |
| [python-port-scanner.md](python-port-scanner.md) | Python TCP port scanner explanation |
| [python-banner-grabber.md](python-banner-grabber.md) | Python HTTP banner grabbing |
| [python-reverse-dns.md](python-reverse-dns.md) | Python reverse DNS lookup |
| [python-security-tools/](python-security-tools/) | Python networking and cybersecurity scripts |
| [screenshots/](screenshots/) | Screenshots from practical labs |

## Python Security Tools

| Script | Purpose |
|---|---|
| [tcp-client.py](python-security-tools/tcp-client.py) | Connects to a TCP service using Python sockets |
| [tcp-server.py](python-security-tools/tcp-server.py) | Creates a simple TCP server for local testing |
| [port-scanner.py](python-security-tools/port-scanner.py) | Checks open TCP ports on a target host |
| [banner-grabber.py](python-security-tools/banner-grabber.py) | Reads basic HTTP service banners |
| [reverse-dns.py](python-security-tools/reverse-dns.py) | Performs reverse DNS lookup for an IP address |

## Topics Practiced

- Linux command line
- Linux permissions
- Process management
- TCP/IP networking
- TCP and UDP traffic
- Listening ports and active connections
- HTTP, HTTPS and TLS basics
- DNS, ICMP and ARP analysis
- Packet capture and filtering
- Wireshark protocol inspection
- tcpdump filtering
- Socket programming
- Python networking scripts
- Port scanning
- Banner grabbing
- Reverse DNS lookup
- Basic troubleshooting
## Screenshots and Lab Evidence

### Wireshark Analysis

#### TCP Conversations Analysis
<img width="1275" height="761" alt="Wireshark TCP conversations analysis" src="https://github.com/user-attachments/assets/61ed6523-6f11-4fb3-814c-e23eded32c01" />

#### DNS Query Analysis
<img width="1268" height="762" alt="Wireshark DNS query analysis" src="https://github.com/user-attachments/assets/db6cbc45-83a5-495e-95c7-a0134cfdac39" />

#### TCP Handshake Analysis
<img width="1269" height="763" alt="Wireshark TCP handshake analysis" src="https://github.com/user-attachments/assets/4874adde-4acd-4a30-ac35-d41f8a8df15c" />

#### HTTP GET Request Analysis
<img width="1273" height="764" alt="Wireshark HTTP GET request analysis" src="https://github.com/user-attachments/assets/36d9bbdc-289f-4035-a73d-af9d29e3bbfc" />

#### TLS Encrypted Traffic Analysis
<img width="1269" height="752" alt="Wireshark TLS encrypted traffic analysis" src="https://github.com/user-attachments/assets/161a2273-3c80-482a-92af-480a7510aefd" />

### Python Networking

#### Python TCP Client
<img width="1274" height="755" alt="Python TCP client execution" src="https://github.com/user-attachments/assets/19ad5ae9-2650-4469-be33-9955e207cba1" />

#### Python Port Scanner
<img width="1273" height="755" alt="Python port scanner execution" src="https://github.com/user-attachments/assets/3ab17205-cd84-4b68-a1d6-231a8280df05" />

#### Python Banner Grabber
<img width="1281" height="763" alt="Python banner grabber execution" src="https://github.com/user-attachments/assets/f89ca935-e2a2-446f-ad60-6f40717d875f" />

#### Python Reverse DNS Lookup
<img width="1282" height="423" alt="Python reverse DNS lookup execution" src="https://github.com/user-attachments/assets/cd290c59-daf1-4633-a900-8e198b84930c" />

### Linux Process and Network Analysis

#### Linux Listening Ports
<img width="1273" height="759" alt="Linux listening ports analysis" src="https://github.com/user-attachments/assets/aa78a61c-1177-4a7f-85dc-66f23ced5b07" />

#### Linux Process and Network Correlation
<img width="1273" height="757" alt="Linux process and network correlation" src="https://github.com/user-attachments/assets/75f741a0-fbb4-4622-96bb-b1941e07e83c" />

#### Linux Process Signal Management
<img width="1273" height="762" alt="Linux process signal management" src="https://github.com/user-attachments/assets/11be06c0-4eaa-4e72-accb-96c83f9552f1" />

### Nmap Scanning

#### Basic Nmap Scan
<img width="1275" height="761" alt="Basic Nmap scan" src="https://github.com/user-attachments/assets/ffb5f38c-6fa0-4394-bd89-50f82175ee0b" />

#### SYN Stealth Scan
<img width="1274" height="760" alt="Nmap SYN stealth scan" src="https://github.com/user-attachments/assets/3163051a-a9d3-45c1-940d-6ecb5a15fa43" />

### tcpdump Analysis

#### ICMP Packet Capture
<img width="1275" height="770" alt="tcpdump ICMP packet capture" src="https://github.com/user-attachments/assets/788126ec-67f5-453a-8cb1-27609b8c43ef" />

#### ICMP and DNS Filtering
<img width="1273" height="764" alt="tcpdump ICMP and DNS filtering" src="https://github.com/user-attachments/assets/e83d3c62-32b5-43db-83c2-e1d392da17ed" />

## Current Learning Roadmap

- Advanced Wireshark analysis
- Python automation
- Bash scripting
- Network monitoring
- Web security basics
- TryHackMe labs
- Linux administration
- Log analysis
- SOC fundamentals

## Goal

Build practical cybersecurity and networking skills through:

- real lab activities
- packet analysis
- Linux administration
- Python scripting
- troubleshooting
- technical documentation

This repository is used as a personal cybersecurity portfolio and learning tracker.

## Disclaimer

This repository is intended for educational purposes only. All activities are performed in controlled laboratory environments.
