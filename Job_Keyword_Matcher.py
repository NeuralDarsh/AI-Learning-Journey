# Practicing Set Operations and Text Analysis for Career Planning

def analyze_job_fit():
    # 1. Your current skill set
    my_skills = {"python", "ai", "ml", "iot", "rdbms", "n5 japanese", "github"}
    
    print("---  Japan IT Job Keyword Matcher ---")
    
    # 2. Simulated Job Description Keywords (e.g., from a Tokyo AI Startup)
    job_keywords = {"python", "pytorch", "ml", "japanese", "docker", "rdbms", "git"}
    
    # 3. Find Matches using Set Intersection
    matches = my_skills.intersection(job_keywords)
    
    # 4. Find Missing Skills using Set Difference
    missing = job_keywords.difference(my_skills)
    
    # 5. Calculate Match Percentage
    match_score = (len(matches) / len(job_keywords)) * 100

    print(f"\nTarget Job Keywords: {job_keywords}")
    print(f"Matched Skills: {matches}")
    print(f"Match Score: {match_score:.2f}%")

    if match_score < 70:
        print(f"\n Focus Area: To land this job, consider learning: {missing}")
    else:
        print("\n Strong Match! You are ready to apply for this role in Japan.")

if __name__ == "__main__":
    analyze_job_fit()