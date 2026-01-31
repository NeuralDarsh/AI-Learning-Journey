# Concept: Python Dictionaries & For Loops

def run_quiz():
    # A Dictionary stores 'Keys' and 'Values' (Core 4th Sem concept)
    vocab = {
        "Neko": "Cat",
        "Mizu": "Water",
        "Taberu": "To eat",
        "Nihongo": "Japanese language",
        "Inaka": "Countryside"
    }
    
    score = 0
    print("--- 🇯🇵 Quick N5 Vocab Quiz ---")
    
    # The 'For Loop' iterates through the dictionary
    for word, meaning in vocab.items():
        answer = input(f"What does '{word}' mean? ").strip().capitalize()
        
        if answer == meaning:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. It means '{meaning}'")
            
    print(f"\nFinal Score: {score}/{len(vocab)}")
    print("Goal: Keeping the Japan dream alive !!")

if __name__ == "__main__":
    run_quiz()