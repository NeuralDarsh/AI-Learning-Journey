# Concept: Nested Dictionaries & Recommendation Logic

def get_recommendation():

    destinations = {
        "romantic": {
            "place": "Tokyo Tower",
            "activity": "Watching the city lights",
            "vibe": " Magical"
        },
        "peaceful": {
            "place": "Meiji Jingu Shrine",
            "activity": "A quiet walk through the forest",
            "vibe": " Zen"
        },
        "sarcastic": {
            "place": "Akihabara Maid Cafe",
            "activity": "Dealing with extreme cuteness",
            "vibe": " Hilarious"
        }
    }

    print("--- 🗼 Tokyo Mood-Based Planner ---")
    mood = input("What's the vibe today? (romantic / peaceful / sarcastic): ").lower()

    # Accessing Nested Data
    if mood in destinations:
        info = destinations[mood]
        print(f"\nTarget Destination: {info['place']}")
        print(f"Plan: {info['activity']}")
        print(f"Vibe Check: {info['vibe']}")
    else:
        print("\nInvalid mood! Maybe try anything else !!")

if __name__ == "__main__":
    get_recommendation()