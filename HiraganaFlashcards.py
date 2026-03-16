# Using random library to practice N5 Hiragana characters

import random

def start_quiz():
    # Dictionary of Hiragana and their Romaji sounds
    hiragana_chars = {
        "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
        "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
        "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so"
    }

    print("--- 🇯🇵 Hiragana Flashcards (N5 Level) 🇯🇵 ---")
    print("Type the Romaji for the character. Type 'exit' to stop.\n")

    chars = list(hiragana_chars.keys())
    score = 0
    total = 0

    while True:
        char = random.choice(chars)
        answer = input(f"What is the sound of '{char}'? ").lower().strip()

        if answer == 'exit':
            break
        
        if answer == hiragana_chars[char]:
            print(" 正解 (Seikai)! Correct.")
            score += 1
        else:
            print(f" 違い (Chigai)! It was '{hiragana_chars[char]}'.")
        
        total += 1

    print(f"\nSession Summary: {score}/{total} correct. Keep practicing!")

if __name__ == "__main__":
    start_quiz()