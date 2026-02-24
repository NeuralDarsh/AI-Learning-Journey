# A script to check if a URL is live or down

import requests

def check_status(url):
    try:
        # Ensure the URL starts with http or https
        if not url.startswith("http"):
            url = "https://" + url
            
        print(f"Checking status of: {url}...")
        response = requests.get(url, timeout=5)
        
        # 200 is the standard 'OK' status code
        if response.status_code == 200:
            print(f"Result: {url} is LIVE! (Status Code: 200)")
        else:
            print(f"Result: {url} returned an error. (Status Code: {response.status_code})")
            
    except requests.exceptions.ConnectionError:
        print(f"Result: {url} is DOWN or the URL is invalid.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_site = input("Enter the website URL to check (e.g., google.com): ")
    check_status(target_site)