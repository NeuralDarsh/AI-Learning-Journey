# Practicing Standardized String Formatting for Professional Dev Workflows

def generate_commit():
    print("---  Professional GitHub Commit Generator ---")
    
    # 1. Standard Type Mapping
    # Common prefixes used in professional Japanese/Global tech teams
    prefixes = {
        "1": "feat: (A new feature)",
        "2": "fix: (A bug fix)",
        "3": "docs: (Changes to documentation)",
        "4": "refactor: (Code change that neither fixes a bug nor adds a feature)",
        "5": "chore: (Updating build tasks, package manager configs, etc.)"
    }

    print("\nSelect the type of change:")
    for key, value in prefixes.items():
        print(f"{key}. {value}")

    choice = input("\nEnter choice (1-5): ")
    
    if choice in prefixes:
        # 2. Collect description
        type_str = prefixes[choice].split(":")[0]
        message = input("Enter a short description of the work: ").strip()
        
        # 3. Format the final string
        final_commit = f"{type_str}: {message}"
        
        print("\n Standardized Commit Message:")
        print(f'>>> git commit -m "{final_commit}"')
    else:
        print(" Invalid selection.")

if __name__ == "__main__":
    generate_commit()