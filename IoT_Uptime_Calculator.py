# Practicing Time Delta calculations and Percentage Logic

import time
from datetime import datetime, timedelta

def calculate_reliability(start_time, total_downtime_minutes):
    # 1. Calculate total elapsed time
    now = datetime.now()
    uptime_duration = now - start_time
    total_seconds = uptime_duration.total_seconds()
    total_minutes = total_seconds / 60

    # 2. Calculate Uptime Percentage
    # Formula: ((Total Time - Downtime) / Total Time) * 100
    if total_minutes > 0:
        uptime_percent = ((total_minutes - total_downtime_minutes) / total_minutes) * 100
    else:
        uptime_percent = 100.0

    print(f"---  IoT Device Reliability Report ---")
    print(f"Device Started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Current Time:   {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Uptime:   {uptime_duration}")
    print(f"Downtime:       {total_downtime_minutes} minutes")
    
    # 3. Output Reliability Status
    print(f"\nReliability Score: {uptime_percent:.2f}%")
    
    if uptime_percent >= 99.9:
        print("Status:  EXCELLENT (Enterprise Grade)")
    elif uptime_percent >= 95:
        print("Status:  STABLE (Maintenance Recommended)")
    else:
        print("Status:  CRITICAL (High Failure Rate)")

if __name__ == "__main__":
    # Simulate a device that started 5 days ago
    start_date = datetime.now() - timedelta(days=5)
    # Simulate 15 minutes of downtime during that period
    calculate_reliability(start_date, 15)