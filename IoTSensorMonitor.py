# Simulating sensor data processing and threshold alerts

import random
import time

def monitor_sensor(threshold):
    print(f"---  IoT Monitor Started (Threshold: {threshold}°C) ---")
    
    # Simulating 5 sensor readings
    for i in range(1, 6):
        current_temp = random.randint(20, 45)
        status = "NORMAL"
        
        if current_temp > threshold:
            status = " ALERT: OVERHEAT"
            # Log the alert to a file (File I/O practice)
            with open("sensor_logs.txt", "a") as log_file:
                log_file.write(f"Alert at Reading {i}: {current_temp}°C\n")
        
        print(f"Reading {i}: {current_temp}°C | Status: {status}")
        time.sleep(1) # Wait 1 second between readings

if __name__ == "__main__":
    # In a real IoT setup, this threshold might come from a mobile app
    user_threshold = int(input("Set Temperature Threshold (e.g., 35): "))
    monitor_sensor(user_threshold)