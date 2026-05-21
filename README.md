# Home Cyber Lab

Personal cybersecurity laboratory built with VirtualBox, Kali Linux and Python.

This repository documents my hands-on learning path in Linux, networking, packet analysis and basic cybersecurity tooling. The goal is to show practical work, clear documentation and steady progress through real lab activities.

## Project Overview

This lab focuses on practical foundations for cybersecurity:

| Area | What I Practiced | Main Evidence |
|---|---|---|
| Kali Linux Lab | virtual machine setup, lab environment and basic configuration | [Kali setup](lab-setup/kali-setup.md) |
| Linux | terminal usage, permissions, processes and signals | [Linux commands](linux-commands.md), [process management](linux-process-management.md) |
| Networking | TCP/IP, DNS, HTTP/HTTPS, ICMP, ARP and ports | [networking basics](networking-basics.md), [TCP/UDP](tcp-udp.md), [listening ports](listening-ports.md), [HTTP/HTTPS](http-https.md) |
| Scanning | basic Nmap scans, listening ports and service discovery | [Nmap basics](nmap-basics.md) |
| Packet Analysis | Wireshark and tcpdump packet capture and filtering | [Wireshark basics](wireshark-basics.md), [tcpdump basics](tcpdump-basics.md) |
| Python | sockets, TCP client/server, port scanning, banner grabbing and reverse DNS | [Python tools folder](python-security-tools/) |
| Lab Evidence | screenshots from practical exercises | [screenshots index](screenshots.md) |

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

| Section | Open | Description |
|---|---|---|
| Lab Setup | [lab-setup/](lab-setup/) | Kali Linux installation and virtual machine configuration |
| Linux Fundamentals | [linux-commands.md](linux-commands.md) | Essential Linux commands and shell basics |
| Linux Processes | [linux-process-management.md](linux-process-management.md) | Linux processes, PID and signal management |
| Networking Fundamentals | [networking-basics.md](networking-basics.md) | Core networking concepts |
| TCP and UDP | [tcp-udp.md](tcp-udp.md) | TCP and UDP fundamentals |
| Listening Ports | [listening-ports.md](listening-ports.md) | Listening ports and active network connections |
| HTTP and HTTPS | [http-https.md](http-https.md) | HTTP, HTTPS and TLS basics |
| Nmap Scanning | [nmap-basics.md](nmap-basics.md) | Introduction to Nmap scanning |
| Wireshark Analysis | [wireshark-basics.md](wireshark-basics.md) | Wireshark packet analysis and protocol inspection |
| tcpdump Analysis | [tcpdump-basics.md](tcpdump-basics.md) | Packet capture and filtering with tcpdump |
| Python Security Tools | [python-security-tools/](python-security-tools/) | Python networking and cybersecurity scripts |
| Screenshots and Evidence | [screenshots.md](screenshots.md) | Organized screenshots from practical labs |

## Python Security Tools

| Script | Purpose |
|---|---|
| [tcp-client.py](python-security-tools/tcp-client.py) | Connects to a TCP service using Python sockets |
| [tcp-server.py](python-security-tools/tcp-server.py) | Creates a simple TCP server for local testing |
| [port-scanner.py](python-security-tools/port-scanner.py) | Checks open TCP ports on a target host |
| [banner-grabber.py](python-security-tools/banner-grabber.py) | Reads basic HTTP service banners |
| [reverse-dns.py](python-security-tools/reverse-dns.py) | Performs reverse DNS lookup for an IP address |

## Lab Evidence

Screenshots are collected in one organized index instead of being loaded directly inside this main README.

| Evidence Page | Description |
|---|---|
| [screenshots.md](screenshots.md) | Linux, networking, Nmap, Wireshark, tcpdump and Python lab screenshots |

## Current Learning Roadmap

| Area | Next Focus |
|---|---|
| Wireshark | Deeper packet analysis and protocol filtering |
| Python | More automation and security-focused scripts |
| Bash | Basic scripting for Linux administration |
| Monitoring | Network monitoring and log review |
| Web Security | HTTP, HTTPS and beginner web security concepts |
| TryHackMe | Beginner labs and writeups |
| SOC Fundamentals | Alerts, logs, investigation workflow and documentation |

## Goal

| Goal | Description |
|---|---|
| Practical Skills | Build cybersecurity and networking skills through real lab activities |
| Documentation | Write clear notes, explanations and technical summaries |
| Analysis | Practice packet capture, protocol inspection and troubleshooting |
| Automation | Create small Python tools for networking and security exercises |
| Portfolio | Use this repository as a personal cybersecurity learning tracker |

## Disclaimer

This repository is intended for educational purposes only. All activities are performed in controlled laboratory environments.
