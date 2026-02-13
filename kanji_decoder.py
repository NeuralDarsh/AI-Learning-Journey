# Concept: Python Dictionaries (Key-Value Pairs)

def decode_kanji():
    # A Dictionary of N5 Kanji (4th Sem concept: Dicts)
    kanji_data = {
        "日": "Sun / Day",
        "本": "Book / Origin",
        "学": "Study / Learning",
        "人": "Person",
        "大": "Big / Great"
    }

    print("--- 🎌 Kanji Decoder System ---")
    search = input("Enter a Kanji to decode (e.g., 日, 本, 学): ")

    # Using the .get() method (Safer way to access dictionary data)
    meaning = kanji_data.get(search, "Kanji not found in N5 database.")
    
    print(f"\nResult: {search} -> {meaning}")
    
    # Logic for your specific goal
    if search == "日" or search == "本":
        print("💡 Fact: '日本' (Nippon) combines these to mean 'Origin of the Sun'!")

if __name__ == "__main__":
    decode_kanji()