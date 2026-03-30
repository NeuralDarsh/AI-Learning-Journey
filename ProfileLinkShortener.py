# Practicing Dictionary mapping and String formatting

def link_shortener():
    # 1. Your personal professional database
    profiles = {
        "gh": "https://github.com/darshan-bagale", # Replace with your actual GitHub
        "li": "https://www.linkedin.com/in/darshan-bagale", # Replace with your LinkedIn
        "n5": "https://jlpt.jp/n5-resources",
    }

    print("---  Darshan's Profile Shortener ---")
    print("Available Codes: gh, li, n5")
    
    code = input("\nEnter the short code: ").lower().strip()

    # 2. Logic to "Redirect"
    if code in profiles:
        print(f"\n Found! Your full URL is:")
        print(f" {profiles[code]}")
        print("\n(In a web app, this would now redirect the user!)")
    else:
        print(" Error: Code not found. Please check your spelling.")

if __name__ == "__main__":
    link_shortener()