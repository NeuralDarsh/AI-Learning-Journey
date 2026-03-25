# Combining OOP, File Handling, and Career Goals

import datetime

class CareerGoal:
    def __init__(self):
        self.milestones = {
            "Japanese Proficiency": "N5",
            "GitHub Streak": "Day 50",
            "LinkedIn Activity": "Daily",
            "Degree": "B.Tech AI & ML"
        }

    def save_milestone(self, note):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("career_milestones.txt", "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] Milestone 50: {note}\n")
        print(" Progress successfully logged to career_milestones.txt")

    def show_dashboard(self):
        print("\n---  JAPAN CAREER DASHBOARD  ---")
        for goal, status in self.milestones.items():
            print(f" {goal}: {status}")
        print("---------------------------------------------")
        print("Status: 50% Complete. Ganbatte kudasai! (Keep going!)")

if __name__ == "__main__":
    my_journey = CareerGoal()
    my_journey.show_dashboard()
    
    # Celebrate the milestone
    celebration_note = "Reached Day 50 of the GitHub Challenge! Halfway to my dream."
    my_journey.save_milestone(celebration_note)