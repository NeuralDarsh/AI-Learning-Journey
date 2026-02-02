# Concept: Linear Scaling & Data Input

def calculate_n5_status():
    print("--- Japanese N5 Goal Progress ---")
    
    # Total targets for N5 level
    total_kanji_target = 100 
    total_vocab_target = 800
    
    # User Inputs (4th Sem Python Practice)
    kanji_done = int(input("How many Kanji have you learned? "))
    vocab_done = int(input("How many Vocab words have you learned? "))
    
    # Linear scaling: (Current / Total) * 100
    kanji_pct = (kanji_done / total_kanji_target) * 100
    vocab_pct = (vocab_done / total_vocab_target) * 100
    
    # Average Progress
    overall = (kanji_pct + vocab_pct) / 2
    
    print(f"\n--- Progress Report ---")
    print(f"Kanji: {kanji_pct:.1f}%")
    print(f"Vocab: {vocab_pct:.1f}%")
    print(f"Overall N5 Readiness: {overall:.1f}%")
    
    if overall >= 80:
        print("Status: You are ready for the JLPT N5 exam! 🎫")
    else:
        print("Status: Keep practicing daily for your quiet life in Japan. 🏔️")

if __name__ == "__main__":
    calculate_n5_status()