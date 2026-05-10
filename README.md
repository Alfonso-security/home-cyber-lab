# 🛡️ Home Cyber Lab

Personal cybersecurity laboratory built using VirtualBox and Kali Linux.

This repository documents my practical learning journey in:

- Linux fundamentals
- Process management
- Networking
- TCP/UDP
- Listening ports
- HTTP/HTTPS
- Nmap
- Basic cybersecurity concepts

The goal of this project is to develop hands-on cybersecurity skills through a controlled lab environment and real command-line/network analysis practice.

---

# 🖥️ Lab Environment

| Component | Details |
|---|---|
| Host OS | Windows |
| Virtualization | VirtualBox |
| Guest OS | Kali Linux |
| RAM | 4 GB |
| CPU | 2 vCPU |
| Network Mode | NAT |
| Purpose | Personal cybersecurity laboratory |

---

# 📂 Repository Structure

| File / Folder | Description |
|---|---|
| [kali-setup.md](kali-setup.md) | Kali Linux installation and VM setup |
| [linux-commands.md](linux-commands.md) | Essential Linux commands |
| [linux-process-management.md](linux-process-management.md) | Linux process and job management |
| [networking-basics.md](networking-basics.md) | Networking fundamentals |
| [tcp-udp.md](tcp-udp.md) | TCP vs UDP concepts |
| [listening-ports.md](listening-ports.md) | Listening ports and active connections |
| [http-https.md](http-https.md) | HTTP, HTTPS and TLS basics |
| [nmap-basics.md](nmap-basics.md) | Nmap introduction and scans |
| [screenshots/](screenshots/) | Practical lab screenshots |
| [screenshots/linux/](screenshots/linux/) | Linux screenshots |
| [screenshots/processes/](screenshots/processes/) | Process management screenshots |
| [screenshots/networking/](screenshots/networking/) | Networking screenshots |
| [screenshots/web/](screenshots/web/) | HTTP/HTTPS screenshots |
| [screenshots/nmap/](screenshots/nmap/) | Nmap screenshots |

---

# 📸 Screenshots

## Linux Permissions

```bash
chmod +x file.sh
ls -l
```

![Linux Permissions](screenshots/linux/chmod-execute-permissions.png)

---

## Active TCP Connections

```bash
ss -tanp
```

![TCP Connections](screenshots/networking/ss-tanp-established-connections.png)

---

## TCP and UDP Connections

```bash
ss -t
ss -u
ss -tan
```

![TCP and UDP Comparison](screenshots/networking/ss-tcp-udp-connections-comparison.png)

---

## Basic Nmap Scan

```bash
nmap scanme.nmap.org
```

![Nmap Scan](screenshots/nmap/nmap-open-port-results.png)

---

## SYN Stealth Scan

```bash
sudo nmap -sS scanme.nmap.org
```

![Nmap SYN Scan](screenshots/nmap/nmap-syn-stealth-scan-progress.png)

---

# 🚀 Skills Practiced

- Linux command line
- Linux permissions
- Bash basics
- Process management
- TCP/UDP networking
- Listening ports
- HTTP/HTTPS analysis
- Nmap scanning
- Network enumeration
- Basic troubleshooting

---

# 📚 Current Learning Roadmap

- Wireshark packet analysis
- Advanced Nmap scans
- Web security basics
- Python for cybersecurity
- TryHackMe labs
- Linux intermediate administration
- Log analysis

---

# ⚠️ Disclaimer

This repository is intended for educational purposes only inside a controlled laboratory environment.
