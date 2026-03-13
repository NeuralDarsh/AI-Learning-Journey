# Practicing Computer Networks concepts (TCP/IP and Ports)

import socket

def scan_ports(host):
    # Common ports to check: 21 (FTP), 22 (SSH), 80 (HTTP), 443 (HTTPS)
    common_ports = [21, 22, 80, 443, 3306]
    
    print(f"--- Scanning common ports on: {host} ---")
    
    for port in common_ports:
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Don't wait more than 1 second
        
        # result of 0 means the port is open
        result = s.connect_ex((host, port))
        
        if result == 0:
            print(f"Port {port}: OPEN ")
        else:
            print(f"Port {port}: Closed/Filtered ")
        
        s.close()

if __name__ == "__main__":
    # '127.0.0.1' is the standard IP address for 'localhost' (your own computer)
    target = "127.0.0.1"
    scan_ports(target)