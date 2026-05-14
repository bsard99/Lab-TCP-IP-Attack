# Lab-TCP-IP-Attack

## Lab Overview
This project explores common vulnerabilities within the TCP protocol. I performed a SYN Flood Denial-of-Service (DoS) attack and established a reverse shell connection to demonstrate how protocol-level weaknesses can be exploited to disrupt services and gain unauthorized access.

## Technical Skills Demonstrated
* **Protocol Analysis:** TCP Three-Way Handshake, SYN/ACK mechanisms.
* **Scripting:** Developed automated attack scripts using **Python** and the **Scapy** library.
* **Environment:** Conducted in a containerized environment using **Docker** (SEED Labs).
* **Tools:** Wireshark, Netcat (nc), Scapy, Linux/Ubuntu.

## Lab Components

### 1. TCP SYN Flood Attack (DoS)
I developed a Python script (`synflood.py`) to overwhelm a target server by sending a high volume of spoofed SYN packets.
* **Logic:** The script randomized source IP addresses, source ports, and sequence numbers to bypass basic filtering and fill the target's TCP connection queue.
* **Result:** Successfully exhausted the server's resources, preventing legitimate users from establishing connections.

### 2. Reverse Shell Execution
I demonstrated a reverse shell attack where a victim machine initiates a connection back to the attacker's machine.
* **Method:** Used Netcat to listen for incoming connections and redirected the victim's bash shell input/output to the network socket.
* **Impact:** Gained remote command-line access to the victim machine, allowing for post-exploitation activities like `whoami` and `hostname` verification.

## Defensive Observations
As a security analyst, these attacks can be detected by:
* **SYN Flooding:** Monitoring for high rates of SYN packets without corresponding ACK completions.
* **Reverse Shells:** Detecting unusual outbound traffic from internal servers to unknown external IPs on common listening ports (e.g., 9090).
