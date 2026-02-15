# Concept: *args (Variable number of arguments)

def total_expenses(*expenses):
    """
    Using *args to sum up a flexible list of costs.
    """
    grand_total = sum(expenses)
    print(f"Number of items tracked: {len(expenses)}")
    return grand_total

def main():
    print("--- 💴 Japan Expense Aggregator ---")
    
    # Simulating different costs: Food, Transport, SIM card, etc.
    # We can pass 3, 5, or 10 numbers; *args handles them all.
    total = total_expenses(1200, 500, 2500, 800)
    
    print(f"Grand Total: ¥{total:,}")
    print("\nDocumentation: Using *args makes this code scalable for AI data inputs.")

if __name__ == "__main__":
    main()