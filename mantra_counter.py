# Concept: Recursion (Functions calling themselves)

def chant_round(bead_number):
    """
    Recursive function to count 108 beads in a round.
    """
    if bead_number > 108:
        print("\n✨ Round Complete! Hare Krishna! ✨")
        return
    
    # In a real app, this would wait for a button click
    print(f"Bead {bead_number}: Hare Krishna Hare Krishna Krishna Krishna Hare Hare...")
    
    # The function calls itself (Recursion)
    chant_round(bead_number + 1)

def main():
    print("--- 🙏 ISKCON Daily Japa Tracker ---")
    start = input("Are you ready to start your round? (yes/no): ").lower()
    
    if start == "yes":
        # We start at bead 1
        chant_round(1)
    else:
        print("Take your time. Consistency is power (Keizoku wa chikara nari)!")

if __name__ == "__main__":
    main()