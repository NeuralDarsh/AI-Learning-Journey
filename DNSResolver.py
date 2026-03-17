# Exploring Computer Networks using Python's socket library

import socket

def get_ip_address(hostname):
    try:
        # The core networking function to resolve a domain
        ip_address = socket.gethostbyname(hostname)
        print(f"---  DNS Resolution ---")
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
    except socket.gaierror:
        print(f" Error: Could not resolve hostname '{hostname}'. Check your connection.")

if __name__ == "__main__":
    print("Welcome to the Python DNS Resolver!")
    url = input("Enter a website URL (e.g., github.com): ").strip()
    
    # Remove https:// or http:// if the user adds it
    clean_url = url.replace("https://", "").replace("http://", "").split('/')[0]
    
    get_ip_address(clean_url)