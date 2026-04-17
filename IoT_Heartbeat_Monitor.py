# Practicing Dictionary State Tracking and Time-based Logic

import time
from datetime import datetime

def monitor_devices():
    # 1. Device Database: {Device_ID: Last_Seen_Timestamp}
    devices = {
        "Sensor_01": time.time(),
        "Sensor_02": time.time(),
        "Gateway_01": time.time()
    }
    
    # 2. Threshold for "Offline" status (e.g., 5 seconds)
    timeout_limit = 5 

    print("---  IoT Heartbeat Monitor ---")
    print(f"Monitoring started at: {datetime.now().strftime('%H:%M:%S')}\n")

    try:
        while True:
            current_time = time.time()
            print(f"\nChecking Status at {datetime.now().strftime('%H:%M:%S')}...")
            
            for device, last_seen in devices.items():
                time_diff = current_time - last_seen
                
                # 3. Check if device is still alive
                if time_diff > timeout_limit:
                    status = " OFFLINE (Alert Sent!)"
                else:
                    status = f" ONLINE (Last seen {int(time_diff)}s ago)"
                
                print(f"{device}: {status}")
            
            # Wait 3 seconds before next check
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\n Monitor stopped. System shutting down...")

if __name__ == "__main__":
    monitor_devices()