# Concept: File Writing (I/O Operations)

import datetime # To automatically add the date

def write_diary_entry():
    # Getting current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("--- 📔 Japan Goal: Daily Reflection ---")
    entry = input("What did you do today to get closer to your quiet life in Japan? ")

    # 'a' stands for 'append' - it adds to the file without deleting old entries
    with open("my_journey.txt", "a") as file:
        file.write(f"[{current_time}] {entry}\n")
    
    print("\n✅ Entry saved successfully to 'my_journey.txt'!")
    print("Check your folder to see the new file!")

if __name__ == "__main__":
    write_diary_entry()