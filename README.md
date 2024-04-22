# ARP Spoofing

## How to run?

```
python3 arp_spoofing_topo.py
```

It will open three terminals: router (root namespace), client, and attacker.

## Tasks:

### How do you check the ARP cache of the client?

### How do you request the MAC address of the router without using L3 (ping, traceroute, ...) or L4/L7 (nc, telnet, curl, ...)?

### How do you spoof the router from the attacker?

# DNS Spoofing

## How to run?

```
python3 dns_spoofing_topo.py
```

It will open four terminals: router (root namespace), dns (root namespace, running DNS server), client, and attacker (running a DNS server that always answers 10.0.1.2).

## Tasks

### How do you query a domain using 10.0.0.2 as DNS server?

### How do you use the ARP spoofing attack to impersonate the DNS server?

### What do you need to make it work?

### Explain why it is dangerous. Provide an example of using this attack to steal bank credentials in public WiFi/wired networks.

