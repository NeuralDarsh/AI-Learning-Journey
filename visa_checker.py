# Concept: Functions and Boolean Logic

def check_eligibility(degree_status, jlpt_level):
    """
    Function to check basic work visa requirements.
    """
    # Boolean Logic (Core 4th Sem concept)
    has_degree = degree_status.lower() == "yes"
    has_n2 = jlpt_level.upper() in ["N1", "N2", "N3"] # N3 is often a minimum for tech

    if has_degree and has_n2:
        return "High Eligibility: You are ready for the Japanese tech market! 🚀"
    elif has_degree:
        return "Partial Eligibility: Focus on your Japanese language (N3/N2). 📚"
    else:
        return "In Progress: Focus on completing your B.Tech first. 🎓"

def main():
    print("--- 🎌 Japan Work Visa Self-Assessment ---")
    
    # Taking inputs
    degree = input("Do you have a B.Tech degree (or are you in the final year)? (yes/no): ")
    japanese = input("What is your current/target JLPT level? (N5/N4/N3/N2/N1): ")

    # Calling the function
    result = check_eligibility(degree, japanese)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()