import requests 
 # This library lets our code talk to the internet

def get_tokyo_weather():
    # We are using a free weather service
    city = "Tokyo"
    url = f"https://wttr.in/{city}?format=3"
    
    print(f"Connecting to Tokyo Weather Server...")
    
    try:
        # This line sends a 'Request' to the server in Japan
        response = requests.get(url)
        
        # 200 means 'Success' in the world of internet networking
        if response.status_code == 200:
            print("\n--- LIVE TOKYO UPDATE ---")
            print(f"Current Status: {response.text}")
            print(f"Goal: Live A Simple And Quiet Life In Japan ")
        else:
            print("Server is busy. Try again in a few minutes.")
            
    except Exception as e:
        # This handles errors if our internet is disconnected
        print(f"Connection Error: {e}")

# This line actually 'calls' the function to start the program
get_tokyo_weather()
