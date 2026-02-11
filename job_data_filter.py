# Concept: Filtering Lists and Data Validation

def filter_candidates():
    # Mock data: A list of candidate "features" (B.Tech AIML Concept)
    candidates = [
        {"name": "Student A", "skill": "Java", "n_level": 5},
        {"name": "Student B", "skill": "AI/ML", "n_level": 0},
        {"name": "Darshan", "skill": "AI/ML", "n_level": 5}, # That's you!
        {"name": "Student C", "skill": "AI/ML", "n_level": 4}
    ]

    print("--- 🔍 Japan Tech Job Filter ---")
    
    # Filtering for AI/ML skill AND N5 or better Japanese
    qualified = [c for c in candidates if c["skill"] == "AI/ML" and c["n_level"] >= 5]
    
    print(f"Total Candidates: {len(candidates)}")
    print(f"Qualified for Interview: {len(qualified)}")
    
    for person in qualified:
        print(f"✅ Match Found: {person['name']} (Skill: {person['skill']}, JLPT: N{person['n_level']})")

if __name__ == "__main__":
    filter_candidates()