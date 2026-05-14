# Planning the future career in Japan while practicing Python Math

def convert_salary():
    # 1. Current Exchange Rate (Approximate for 2026)
    # 1 JPY = 0.55 INR (Example rate)
    YEN_TO_INR = 0.55 
    
    print("---  Japan Career Financial Planner 🇮🇳 ---")
    
    # 2. Input monthly salary in Yen
    # Average entry-level IT salary in Japan is ~250,000 Yen
    try:
        yen_salary = float(input("Enter expected monthly salary in Yen (¥): "))
        
        # 3. Calculation
        inr_salary = yen_salary * YEN_TO_INR
        annual_inr = inr_salary * 12
        
        print(f"\nMonthly Salary: ₹{inr_salary:,.2f} INR")
        print(f"Annual Salary:  ₹{annual_inr:,.2f} INR")
        
        if yen_salary >= 200000:
            print("\n This is a strong starting salary for a Junior Engineer in Japan!")
        else:
            print("\n Keep building your AI/ML skills to target higher-paying roles.")
            
    except ValueError:
        print("Please enter a valid number for the salary.")

if __name__ == "__main__":
    convert_salary()