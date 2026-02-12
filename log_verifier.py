# Concept: OS Module and Path Validation

import os

def verify_and_log():
    filename = "my_journey.txt"
    
    print("--- 📂 System Check: Japan Journey Log ---")
    
    # Checking if the file exists (4th Sem Python concept)
    if os.path.exists(filename):
        print(f"✅ Found: {filename}. Your history is safe.")
        
        # Calculate file size in bytes
        file_size = os.path.getsize(filename)
        print(f"📊 Current Log Size: {file_size} bytes")
        
        entry = input("\nAdd a quick note for Feb 12: ")
        with open(filename, "a") as file:
            file.write(f"[Verified Feb 12] {entry}\n")
            print("Successfully updated your journey! 🏔️")
    else:
        print(f"❌ Error: {filename} not found in this folder!")
        print("Please run 'goal_diary.py' first to create your log.")

if __name__ == "__main__":
    verify_and_log()