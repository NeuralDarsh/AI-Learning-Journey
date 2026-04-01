# Using random library for daily vocabulary practice

import random
from datetime import date

def get_daily_word():
    # A dictionary of N5 Vocabulary
    # Format: "Kanji/Hiragana": ["Romaji", "English Meaning"]
    vocabulary = {
        "こんにちは": ["Konnichiwa", "Hello / Good afternoon"],
        "ありがとう": ["Arigatou", "Thank you"],
        "がくせい": ["Gakusei", "Student"],
        "べんきょう": ["Benkyou", "Study"],
        "にほんご": ["Nihongo", "Japanese Language"],
        "さくら": ["Sakura", "Cherry Blossom"],
        "せんせい": ["Sensei", "Teacher"],
        "ともだち": ["Tomodachi", "Friend"]
    }

    # Use the current date as a seed so the word only changes once per day
    # Or remove the seed line if you want a new word every time you run it!
    # random.seed(int(date.today().strftime("%Y%m%d")))

    word = random.choice(list(vocabulary.keys()))
    details = vocabulary[word]

    print(f"---  Day 57: Japanese N5 Vocabulary  ---")
    print(f"Today is: {date.today()}")
    print(f"\nWord: {word}")
    print(f"Romaji: {details[0]}")
    print(f"Meaning: {details[1]}")
    print("\n-------------------------------------------")
    print("頑張って! (Ganbatte! - Do your best!)")

if __name__ == "__main__":
    get_daily_word()