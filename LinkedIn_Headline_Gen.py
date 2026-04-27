# Practicing String Templates and Personal Branding Logic

def optimize_headline():
    print("---  LinkedIn Headline Optimizer (Japan Focus) ---")
    
    # 1. User Data
    name = "Darshan Bagale"
    degree = "B.Tech in AI & ML"
    skills = "Python | IoT | RDBMS"
    language = "JLPT N5"
    goal = "Aspiring Software Engineer in Japan"

    # 2. Headline Templates
    # Template A: Skills-focused
    template_a = f"{degree} Student | {skills} | {language} | {goal}"
    
    # Template B: Career-focused (Japanese recruiters often look for specific titles)
    template_b = f"AI & ML Student at DYP | {language} Learner | {goal}"

    # Template C: Short & Precise
    template_c = f"{name} | {degree} | Future IT Professional in Japan"

    print("\nSelect your favorite for your LinkedIn Profile:")
    print("-" * 40)
    print(f"Style 1: {template_a}")
    print(f"Style 2: {template_b}")
    print(f"Style 3: {template_c}")
    print("-" * 40)

if __name__ == "__main__":
    optimize_headline()