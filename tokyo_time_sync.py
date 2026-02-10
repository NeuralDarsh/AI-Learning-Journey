# Concept: Importing Modules & Datetime Objects

import datetime

def show_clocks():
    # Fetching current time in UTC/Local
    now = datetime.datetime.now()
    
    # India is UTC +5:30, Japan is UTC +9:00
    # Japan is exactly 3.5 hours ahead of India
    japan_time = now + datetime.timedelta(hours=3, minutes=30)

    print("--- 🕒 Real-Time Journey Tracker ---")
    print(f"Current Time (India): {now.strftime('%H:%M:%S')}")
    print(f"Current Time (Japan): {japan_time.strftime('%H:%M:%S')}")
    
    print("\n--- 🗾 Daily Goal ---")
    if 9 <= japan_time.hour <= 18:
        print("Status: Business hours in Tokyo. Keep studying to join them! 💼")
    else:
        print("Status: Evening in Tokyo. Perfect time for quiet reflection. 🏔️")

if __name__ == "__main__":
    show_clocks()