# Concept: Custom Sorting with Lambda Functions

def rank_cities():
    # List of tuples: (City Name, Distance from Tokyo in km)
    cities = [
        ("Kyoto", 450),
        ("Osaka", 500),
        ("Yokohama", 30),
        ("Sapporo", 1100),
        ("Fukuoka", 1100)
    ]

    print("---  Japan City Distance Tracker ---")
    print(f"Original List: {cities}")

    # Sorting using a Lambda as the 'key'
    # x[1] tells Python to sort by the second item in each tuple (the distance)
    sorted_cities = sorted(cities, key=lambda x: x[1])

    print("\n---  Cities Sorted by Proximity to Tokyo ---")
    for city, distance in sorted_cities:
        print(f"{city}: {distance} km away")

if __name__ == "__main__":
    rank_cities()