# Practicing dynamic list management and feedback loops

import random

def run_srs_session():
    # 1. New words for today (Katakana for IT)
    study_list = [
        ("サーバー", "Server"),
        ("クラウド", "Cloud"),
        ("アプリ", "App"),
        ("プログラミング", "Programming")
    ]
    
    review_needed = []
    mastered = []

    print("---  Japanese IT Vocabulary SRS Session ---")
    print("Translate the following Katakana to English:\n")

    # 2. First Pass
    for kana, english in study_list:
        answer = input(f"Word: {kana} -> ").strip().lower()
        
        if answer == english.lower():
            print(" Correct! Saved to Mastered.")
            mastered.append(kana)
        else:
            print(f" Not quite. The answer was '{english}'. Adding to Review.")
            review_needed.append((kana, english))

    # 3. Review Loop (The Feedback Loop)
    if review_needed:
        print("\n---  Starting Review Session ---")
        for kana, english in review_needed:
            input(f"Press Enter to see the answer for {kana}...")
            print(f"Meaning: {english}")

    print(f"\nSession Complete! Mastered: {len(mastered)} | Needs Review: {len(review_needed)}")

if __name__ == "__main__":
    run_srs_session()