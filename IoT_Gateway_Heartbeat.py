# Practicing continuous monitoring and status signaling

import time
import datetime

def start_heartbeat():
    print("---  IoT Gateway: Heartbeat Monitoring ---")
    print("Press Ctrl+C to stop the gateway signal.\n")
    
    count = 0
    try:
        while True:
            # 1. Generate timestamp for the heartbeat
            now = datetime.datetime.now().strftime("%H:%M:%S")
            
            # 2. Simulate sending a packet
            count += 1
            print(f"[{now}] Heartbeat #{count}: STATUS_OK (Signal Strength: 98%)")
            
            # 3. Wait for 3 seconds before next signal
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\n Gateway Shutdown: Signal terminated by user.")

if __name__ == "__main__":
    start_heartbeat()