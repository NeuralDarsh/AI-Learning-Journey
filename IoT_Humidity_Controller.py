# Practicing Hysteresis Logic and State Management

import random
import time

def run_controller():
    # 1. Configuration
    UPPER_THRESHOLD = 60.0  # Turn ON fan above this
    LOWER_THRESHOLD = 55.0  # Turn OFF fan below this
    fan_is_on = False

    print("---  IoT Humidity Controller (Hysteresis) ---")
    print(f"High Limit: {UPPER_THRESHOLD}% | Low Limit: {LOWER_THRESHOLD}%")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            # 2. Simulate humidity sensor reading
            current_humidity = round(random.uniform(50.0, 65.0), 2)
            
            # 3. Hysteresis Control Logic
            if current_humidity > UPPER_THRESHOLD and not fan_is_on:
                fan_is_on = True
                action = " HIGH HUMIDITY: Fan turned ON"
            elif current_humidity < LOWER_THRESHOLD and fan_is_on:
                fan_is_on = False
                action = " COMFORTABLE: Fan turned OFF"
            else:
                action = "No change"

            status = "RUNNING" if fan_is_on else "IDLE"
            print(f"Humidity: {current_humidity}% | Fan: {status:<7} | {action}")
            
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n Controller deactivated.")

if __name__ == "__main__":
    run_controller()