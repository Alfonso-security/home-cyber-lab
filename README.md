# 🛡️ Home Cyber Lab

Personal cybersecurity laboratory built using VirtualBox and Kali Linux.

This repository documents my practical learning journey in:

- Linux fundamentals
- Linux process management
- Networking fundamentals
- TCP/UDP protocols
- Listening ports and active connections
- HTTP and HTTPS analysis
- DNS analysis
- ICMP analysis
- ARP analysis
- TCP handshake analysis
- TLS/HTTPS encrypted traffic
- Wireshark packet analysis
- tcpdump packet capture
- Nmap scanning
- Basic cybersecurity concepts

The goal of this project is to develop practical cybersecurity and networking skills through a controlled laboratory environment and real command-line/network traffic analysis.

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
| [wireshark-basics.md](wireshark-basics.md) | Wireshark packet analysis and protocol inspection |
| [tcpdump-basics.md](tcpdump-basics.md) | tcpdump command-line packet capture |
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

## DNS Analysis with Wireshark

```text
dns
```

<img width="1268" height="762" alt="Screenshot 2026-05-10 104627" src="https://github.com/user-attachments/assets/db6cbc45-83a5-495e-95c7-a0134cfdac39" />

---

## TCP Handshake Analysis

```text
tcp
```

<img width="1272" height="761" alt="Screenshot 2026-05-10 115733" src="https://github.com/user-attachments/assets/05c2e537-8543-4cf5-be1b-b24385d3efdf" />

---

## HTTP GET Request Analysis

```bash
curl http://example.com
```

<img width="1273" height="764" alt="Screenshot 2026-05-10 111502" src="https://github.com/user-attachments/assets/36d9bbdc-289f-4035-a73d-af9d29e3bbfc" />

---

## TLS / HTTPS Analysis

```bash
curl https://google.com
```

<img width="1269" height="752" alt="Screenshot 2026-05-10 114403" src="https://github.com/user-attachments/assets/161a2273-3c80-482a-92af-480a7510aefd" />

---

## ICMP Ping Analysis

```bash
ping google.com
```

<img width="1269" height="760" alt="Screenshot 2026-05-10 122023" src="https://github.com/user-attachments/assets/8cae534d-dd57-446a-9e22-ede86345747c" />

---

## tcpdump Live Packet Capture

```bash
sudo tcpdump -i eth0
```

<img width="1275" height="770" alt="Screenshot 2026-05-10 120844" src="https://github.com/user-attachments/assets/788126ec-67f5-453a-8cb1-27609b8c43ef" />

---

## tcpdump Protocol Filtering

```bash
sudo tcpdump -i eth0 icmp
sudo tcpdump -i eth0 port 53
```
<img width="1273" height="764" alt="Screenshot 2026-05-10 121153" src="https://github.com/user-attachments/assets/e83d3c62-32b5-43db-83c2-e1d392da17ed" />


---

# 🚀 Skills Practiced

- Linux command line
- Linux permissions management
- Bash basics
- Linux process management
- TCP/UDP networking
- Listening ports analysis
- TCP handshake analysis
- HTTP/HTTPS analysis
- TLS encrypted traffic analysis
- DNS traffic analysis
- ICMP diagnostics
- ARP analysis
- Wireshark filtering
- Packet capture and inspection
- tcpdump command-line analysis
- Nmap scanning
- Network troubleshooting
- Protocol analysis
- Basic network security concepts

---

# 📚 Current Learning Roadmap

- Advanced Wireshark analysis
- Advanced Nmap scans
- Python for cybersecurity
- TryHackMe labs
- Linux intermediate administration
- Log analysis
- Web security basics
- Network monitoring
- Packet analysis automation

---

# ⚠️ Disclaimer

This repository is intended for educational purposes only inside a controlled personal laboratory environment.
