# Practicing HTTP Requests (Application Layer) for Networking & IoT

import requests
import time

def check_connection(url):
    print(f"---  IoT Connectivity Monitor: {url} ---")
    
    try:
        # Measure time taken for the request
        start_time = time.time()
        response = requests.get(url, timeout=5)
        end_time = time.time()
        
        latency = round((end_time - start_time) * 1000, 2) # in milliseconds
        
        # HTTP Status Codes: 200 is OK, 404 is Not Found, 500 is Server Error
        if response.status_code == 200:
            print(f"Status: ONLINE  | Code: {response.status_code}")
            print(f"Latency: {latency} ms")
        else:
            print(f"Status: ISSUE  | Code: {response.status_code}")

        # Log to file for "Project Management" records
        with open("network_log.txt", "a") as log:
            log.write(f"{time.ctime()} - {url} - {response.status_code} - {latency}ms\n")

    except requests.exceptions.RequestException as e:
        print(f"Status: OFFLINE  | Error: {e}")

if __name__ == "__main__":
    # You can test with Google or GitHub
    target_site = "https://www.google.com"
    check_connection(target_site)