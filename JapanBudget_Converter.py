# Practicing Arithmetic Operations and User Input Handling

def calculate_budget():
    # 1.current conversion rate (Approximate: 1 INR = 1.80 JPY)
    inr_to_jpy_rate = 1.80

    print("---  Japan Travel Budgeter (INR -> JPY)  ---")
    
    try:
        inr_amount = float(input("Enter amount in Indian Rupees (INR): "))
        
        # 2. Perform Conversion
        jpy_amount = inr_amount * inr_to_jpy_rate
        
        print(f"\nTotal in Japanese Yen: ¥{jpy_amount:,.2f}")
        
        # 3. Travel Logic: What can you buy?
        print("\n---  What this gets you in Japan: ---")
        if jpy_amount >= 100000:
            print(" One week of budget accommodation!")
        if jpy_amount >= 50000:
            print(" A 7-day Japan Rail Pass (Green Class)!")
        if jpy_amount >= 1000:
            print(" A delicious bowl of Ramen in Tokyo!")
        else:
            print(" Keep saving! Every Rupee counts toward your Japan dream.")

    except ValueError:
        print("Error: Please enter a valid numerical amount.")

if __name__ == "__main__":
    calculate_budget()