# Concept: Nested Dictionaries & Comparison Logic

def compare_cities():
    # Nested Dictionary (Advanced 4th Sem Python concept)
    cities = {
        "Tokyo": {"density": "High", "vibe": "Busy", "quiet_score": 2},
        "Kyoto": {"density": "Medium", "vibe": "Traditional", "quiet_score": 7},
        "Nagano": {"density": "Low", "vibe": "Peaceful", "quiet_score": 9}
    }
    
    print("---  Japan City Vibe Checker ---")
    print("Available cities: Tokyo, Kyoto, Nagano")
    
    choice = input("Which city are you interested in? ").capitalize()
    
    if choice in cities:
        data = cities[choice]
        print(f"\nResults for {choice}:")
        print(f"- Population Density: {data['density']}")
        print(f"- Atmosphere: {data['vibe']}")
        print(f"- Quiet Life Score: {data['quiet_score']}/10")
        
        if data['quiet_score'] >= 8:
            print("\n This city perfectly matches your 'Inaka' (quiet life) goal!")
        else:
            print("\n This might be a bit too crowded for your preference.")
    else:
        print("City not in our current database. Stick to the roadmap!")

if __name__ == "__main__":
    compare_cities()