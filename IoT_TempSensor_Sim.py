# Practicing IoT Threshold Logic and Data Simulation

import random
import time

def monitor_sensor(threshold):
    print(f"---  IoT Sensor Monitor (Threshold: {threshold}°C) ---")
    print("Press Ctrl+C to stop monitoring.\n")
    
    try:
        while True:
            # 1. Simulate reading from a DHT11 or DHT22 sensor
            current_temp = round(random.uniform(20.0, 40.0), 2)
            
            # 2. Logic: Check if temperature exceeds limit
            if current_temp > threshold:
                status = " ALERT: HIGH TEMP!"
            else:
                status = " Normal"
            
            print(f"Reading: {current_temp}°C | Status: {status}")
            
            # 3. Wait 2 seconds before next "reading" (Sensor Sampling Rate)
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\n Monitoring stopped by user. Device shutting down...")

if __name__ == "__main__":
    # In an industrial IoT setting, we might set this to 35.0°C
    limit = 35.0
    monitor_sensor(limit)