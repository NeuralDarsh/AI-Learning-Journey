# Linear Algebra Tool: Japan Savings & Goal Projection
# Concept: y = mx + b (Simple Linear Regression)

def run_projection():
    print("--- 🇯🇵 Project: Simple & Quiet Life in Japan ---")
    
    # User Inputs for the Linear Equation
    current_balance = float(input("Current Savings (INR): "))
    monthly_save = float(input("Planned Monthly Saving (INR): "))
    time_period = int(input("Months until graduation/move: "))

    # Linear Calculation: y = (m * x) + b
    projected_inr = (monthly_save * time_period) + current_balance
    
    # Currency Conversion (Approx rate)
    projected_jpy = projected_inr * 1.80

    print(f"\n--- 📈 Projection Results ---")
    print(f"Total Projected (INR): ₹{projected_inr:,.2f}")
    print(f"Total Projected (JPY): ¥{projected_jpy:,.2f}")
    
    if projected_jpy >= 500000:
        print("\nStatus: Target reached for initial relocation!")
    else:
        print("\nStatus: Keep building. Every small step counts toward the dream.")

if __name__ == "__main__":
    run_projection()