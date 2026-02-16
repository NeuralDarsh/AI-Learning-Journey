# Concept: **kwargs (Variable Keyword Arguments)

def create_profile(name, city, **details):
    """
    Using **kwargs to add optional details to a university profile.
    """
    print(f"---  University: {name} ({city}) ---")
    
    # kwargs acts like a dictionary
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

def main():
    # We can pass different types of info for different universities
    print(" Generating Education Profiles...\n")
    
    # Profile 1: Basic info
    create_profile("University of Tokyo", "Tokyo", rank=1, type="National")
    
    print("\n" + "-"*30 + "\n")
    
    # Profile 2: More detailed info (the power of **kwargs)
    create_profile("Kyoto University", "Kyoto", 
                   rank=2, 
                   research_focus="AI & Robotics",
                   scholarship="MEXT Available")

if __name__ == "__main__":
    main()