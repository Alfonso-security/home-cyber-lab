# Kali Linux Lab Setup

## Purpose

This document describes the setup of my Kali Linux virtual machine used as the main environment for cybersecurity practice.

The goal is to build a controlled and repeatable lab where I can practice Linux fundamentals, networking, packet analysis and basic security tooling without affecting real systems.

## Lab Environment

| Component | Configuration |
|---|---|
| Host operating system | Windows |
| Virtualization platform | VirtualBox |
| Guest operating system | Kali Linux |
| Memory | 4 GB RAM |
| CPU | 2 virtual cores |
| Virtual disk | 40 GB |
| Network mode | NAT |
| Main use | Cybersecurity practice and network analysis |

## Setup Steps

| Step | Action | Purpose |
|---|---|---|
| 1 | Created a new VirtualBox virtual machine | Prepare an isolated lab machine |
| 2 | Installed Kali Linux | Build the main cybersecurity workstation |
| 3 | Allocated RAM, CPU and disk resources | Keep the VM usable for tools and packet analysis |
| 4 | Configured NAT networking | Allow internet access while keeping the VM isolated |
| 5 | Updated the operating system | Install current package versions and security updates |
| 6 | Tested network connectivity | Confirm the VM can reach external hosts |

## Commands Used

| Command | Reason |
|---|---|
| sudo apt update | Refresh package repositories |
| sudo apt upgrade -y | Upgrade installed packages |
| ip a | Check network interfaces and assigned IP address |
| ping google.com | Verify external network connectivity |

## Network Configuration Notes

| Item | Observation |
|---|---|
| Network mode | NAT |
| VM isolation | The VM is separated from the host network by VirtualBox NAT |
| Internet access | Verified through ping and package updates |
| Lab safety | Activities are performed inside a controlled virtual environment |

## Skills Practiced

| Skill | Evidence |
|---|---|
| Virtualization | Created and configured a Kali Linux VM |
| Linux administration | Updated the system and checked basic configuration |
| Networking basics | Verified IP configuration and connectivity |
| Lab safety | Used an isolated environment for security practice |
| Documentation | Recorded setup steps, commands and purpose |

## Result

The Kali Linux virtual machine is ready to be used as the main home cyber lab environment for Linux practice, networking fundamentals, packet analysis and Python-based security tools.
