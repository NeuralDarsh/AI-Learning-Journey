# Day 6: Japan Habit Tracker
# Concept: Lists and User Validation

def track_habits():
    habits = ["Study ML", "Japanese Practice", "16 Rounds Of Chanting Hare Krishna Mahamantra", "Coding"]
    completed = []

    print("---  My Japan Goal Daily Tracker ---")
    
    for habit in habits:
        status = input(f"Did you finish {habit} today? (y/n): ").lower()
        if status == 'y':
            completed.append(habit) # Adding to a list (4th Sem concept)

    print("\n--- Daily Summary ---")
    print(f"You completed {len(completed)} out of {len(habits)} habits.")
    
    if len(completed) == len(habits):
        print("Amazing! You are moving closer to your quiet life in Japan! 🇯🇵")
    else:
        print("Keep going , Every small step counts!")

if __name__ == "__main__":
    track_habits()