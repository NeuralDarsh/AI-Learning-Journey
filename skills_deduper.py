# Concept: Python Sets (Unique Collections)

def extract_unique_skills():
    # A list with duplicates (maybe you added 'Python' twice by mistake)
    raw_skills = ["Python", "AI", "Japanese", "Machine Learning", "Python", "Japanese", "GitHub"]
    
    print("---  Raw Skill List (With Duplicates) ---")
    print(f"Count: {len(raw_skills)}")
    print(raw_skills)

    # Converting list to set automatically removes duplicates
    unique_skills = set(raw_skills)

    print("\n---  Unique Skill Set ---")
    print(f"Count: {len(unique_skills)}")
    print(unique_skills)

    # Adding a new skill to the set
    new_skill = "N5 Kanji"
    unique_skills.add(new_skill)
    
    print(f"\nAdded '{new_skill}': {unique_skills}")

if __name__ == "__main__":
    extract_unique_skills()