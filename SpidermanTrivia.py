# A fun quiz game to test knowledge of Spider-Man movies and lore

def run_quiz():
    questions = {
        "Who played Spider-Man in the 2002 trilogy?": "Tobey Maguire",
        "What is the civilian name of the Spider-Man from Earth-1610 (Spider-Verse)?": "Miles Morales",
        "Which movie featured all three live-action Spider-Men?": "No Way Home",
        "What is the name of Peter Parker's aunt?": "May",
        "In which city does Spider-Man live?": "New York"
    }

    score = 0
    print("--- 🕷️ Welcome to the Spider-Man Trivia Quiz! 🕷️ ---")
    print("Type your answer and press Enter.\n")

    for question, answer in questions.items():
        user_answer = input(f"{question}: ")
        
        if user_answer.strip().lower() == answer.lower():
            print("✅ Correct! Great job, True Believer!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {answer}")
        print("-" * 30)

    print(f"\nGame Over! Your final score: {score}/{len(questions)}")
    if score == len(questions):
        print("Ultimate Spider-Man status achieved! 🕸️")

if __name__ == "__main__":
    run_quiz()