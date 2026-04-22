# Concept: Error Handling (Try-Except blocks)

def calculate_budget():
    print("--- 💴 Japan Travel Budget Calculator ---")
    
    try:
        # User input could be a mistake (like typing 'abc' instead of a number)
        total_inr = float(input("Enter your savings in INR: "))
        days = int(input("How many days do you plan to stay? "))

        # Math logic
        per_day = total_inr / days
        jpy_total = total_inr * 1.80

        print(f"\n--- 📈 Results ---")
        print(f"Total in Yen: ¥{jpy_total:,.2f}")
        print(f"Daily Budget: ₹{per_day:,.2f}")

    except ValueError:
        # Handles cases where user types text instead of numbers
        print("\n❌ Error: Please enter valid numbers only!")
    except ZeroDivisionError:
        # Handles cases where user types '0' for days
        print("\n❌ Error: Days must be greater than zero!")
    except Exception as e:
        # Catches any other unexpected errors
        print(f"\n❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculate_budget()