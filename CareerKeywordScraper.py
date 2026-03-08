# Simulating how AI filters profiles for specific skills like 'Japan' or 'Python'

def analyze_profile(profile_text, keywords):
    print("--- 🔍 AI Profile Analysis Started ---")
    found_keywords = []
    
    # Convert profile to lowercase for better matching
    profile_lower = profile_text.lower()
    
    for word in keywords:
        if word.lower() in profile_lower:
            found_keywords.append(word)
            
    return found_keywords

if __name__ == "__main__":
    # Example profile text (like your LinkedIn bio)
    my_profile = """
    B.Tech student in AI and ML. Currently learning Japanese (N5) 
    and working on GitHub daily. Interested in Python Programming, 
    IoT, and landing a job in Japan.
    """
    
    # Skills recruiters are looking for
    target_skills = ["Japan", "Python", "N5", "Machine Learning", "IoT", "Java"]
    
    matches = analyze_profile(my_profile, target_skills)
    
    print(f"\nProfile Analysis Result:")
    print(f"Keywords Found: {', '.join(matches)}")
    
    match_percentage = (len(matches) / len(target_skills)) * 100
    print(f"Profile Match Score: {match_percentage:.1f}%")

    if "Japan" in matches and "N5" in matches:
        print("🌟 Recommendation: Strong candidate for Japanese Tech roles!")