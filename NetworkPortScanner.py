# Practicing Socket Programming for Networking & IoT Security

import socket

def scan_ports(target_host, port_list):
    print(f"--- Scanning Host: {target_host} ---")
    
    for port in port_list:
        # 1. Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Wait 1 second for a response
        
        # 2. Attempt to connect to the port
        # connect_ex returns 0 if the connection was successful
        result = sock.connect_ex((target_host, port))
        
        if result == 0:
            print(f"Port {port: <4}: OPEN ")
        else:
            print(f"Port {port: <4}: CLOSED ")
            
        sock.close()

if __name__ == "__main__":
    # Target: Localhost (127.0.0.1) checks your own computer's ports
    target = "127.0.0.1" 
    # Common ports: 80 (HTTP), 443 (HTTPS), 22 (SSH), 21 (FTP), 3306 (MySQL)
    common_ports = [21, 22, 80, 443, 3306]
    
    scan_ports(target, common_ports)