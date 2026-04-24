# Practicing Dictionary Mapping and Randomization for Language Learning

import random

def run_flashcards():
    # 1. Tech-related Katakana Dictionary
    # Key: Katakana, Value: Romaji
    flashcards = {
        "パイソン": "Paison (Python)",
        "コンピュータ": "Konpyuuta (Computer)",
        "エンジニア": "Enjinia (Engineer)",
        "データ": "Deeta (Data)",
        "ネットワーク": "Nettowaaku (Network)",
        "ソフト": "Sofuto (Software)"
    }

    print("--- Katakana IT Vocabulary Flashcards ---")
    print("Type the Romaji meaning or 'exit' to quit.\n")

    # 2. Shuffle and Quiz Logic
    items = list(flashcards.items())
    random.shuffle(items)

    score = 0
    for kana, romaji in items:
        user_answer = input(f"What is the Romaji for '{kana}'? ").strip().lower()
        
        if user_answer == 'exit':
            break
            
        # Check if the answer is inside the romaji string (simple match)
        if user_answer in romaji.lower():
            print(" Correct! 正解 (Seikai)")
            score += 1
        else:
            print(f" Incorrect. The answer is: {romaji}")

    print(f"\n--- Final Score: {score}/{len(flashcards)} ---")

if __name__ == "__main__":
    run_flashcards()