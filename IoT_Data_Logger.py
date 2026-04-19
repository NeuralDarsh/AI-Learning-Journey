# Practicing File I/O (Input/Output) and Data Logging

import random
import time
from datetime import datetime

def log_sensor_data(filename="sensor_log.txt"):
    print(f"---  IoT Data Logger (Saving to {filename}) ---")
    print("Press Ctrl+C to stop logging.\n")

    try:
        # 1. Open file in 'append' mode ('a') so we don't overwrite old data
        with open(filename, "a") as file:
            while True:
                # 2. Generate simulated sensor data
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                temperature = round(random.uniform(22.0, 28.0), 2)
                humidity = round(random.uniform(40.0, 60.0), 2)

                # 3. Format the log entry
                log_entry = f"[{timestamp}] Temp: {temperature}C | Humidity: {humidity}%\n"
                
                # 4. Write to file and flush to ensure it saves immediately
                file.write(log_entry)
                file.flush()
                
                print(f"Logged: {log_entry.strip()}")
                
                # Wait 5 seconds between logs
                time.sleep(5)

    except KeyboardInterrupt:
        print("\n Logging stopped. You can now check 'sensor_log.txt' for your data.")

if __name__ == "__main__":
    log_sensor_data()