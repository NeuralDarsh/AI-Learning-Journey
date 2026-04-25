# Practicing Conditional Monitoring and Alert Logic for IoT Systems

import random
import time

def monitor_temperature(threshold=30.0):
    print(f"---  IoT Temperature Alert System ---")
    print(f"Alert Threshold set to: {threshold}°C\n")

    try:
        while True:
            # 1. Simulate reading from an IoT sensor
            current_temp = round(random.uniform(20.0, 35.0), 2)
            
            # 2. Alert Logic
            if current_temp > threshold:
                status = f" CRITICAL: {current_temp}°C - Sending Alert!"
            elif current_temp > threshold - 5:
                status = f" WARNING: {current_temp}°C - Rising fast."
            else:
                status = f" NORMAL: {current_temp}°C"

            print(status)
            
            # Wait 2 seconds between readings
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n Monitoring stopped by user.")

if __name__ == "__main__":
    # You can change the threshold value here
    monitor_temperature(threshold=28.0)