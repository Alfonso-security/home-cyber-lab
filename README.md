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
| [screenshots.md](screenshots.md) | Practical lab screenshots |


---

# 📸 Screenshots

## Linux Permissions

```bash
chmod +x file.sh
ls -l
```

<img width="1274" height="760" alt="Screenshot 2026-05-10 004906" src="https://github.com/user-attachments/assets/0f8d4df4-cd79-4f96-b18a-f48e517e01e3" />

---

## Active TCP Connections

```bash
ss -tanp
```

<img width="1265" height="757" alt="Screenshot 2026-05-10 012802" src="https://github.com/user-attachments/assets/94bc8aa4-279a-43b4-b43e-f612c865baf0" />

---

## TCP and UDP Connections

```bash
ss -t
ss -u
ss -tan
```

<img width="1265" height="762" alt="Screenshot 2026-05-10 092811" src="https://github.com/user-attachments/assets/49cf76e6-002c-4866-9ac7-1f01dda58d3a" />

---

## Basic Nmap Scan

```bash
nmap scanme.nmap.org
```

<img width="1275" height="761" alt="Screenshot 2026-05-10 021656" src="https://github.com/user-attachments/assets/ffb5f38c-6fa0-4394-bd89-50f82175ee0b" />

---

## SYN Stealth Scan

```bash
sudo nmap -sS scanme.nmap.org
```

<img width="1274" height="760" alt="Screenshot 2026-05-10 022715" src="https://github.com/user-attachments/assets/3163051a-a9d3-45c1-940d-6ecb5a15fa43" />

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
