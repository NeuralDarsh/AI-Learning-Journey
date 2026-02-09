# Concept: List Comprehensions

def convert_savings():
    # A list of savings goals in INR (Indian Rupees)
    inr_goals = [5000, 15000, 50000, 100000, 250000]
    
    # Current Exchange Rate (Approx 1 INR = 1.80 JPY)
    exchange_rate = 1.80
    
    print("--- 💴 Japan Relocation Savings Goals ---")
    print(f"Original (INR): {inr_goals}")
    
    # The 'List Comprehension' - transforms the whole list in one line!
    jpy_goals = [amount * exchange_rate for amount in inr_goals]
    
    print("\n--- Converted Goals (Japanese Yen) ---")
    for original, converted in zip(inr_goals, jpy_goals):
        print(f"₹{original:,}  -->  ¥{converted:,.0f}")
    
    print("\nEvery Rupee saved is a step closer to the quiet life in Japan! 🏔️")

if __name__ == "__main__":
    convert_savings()