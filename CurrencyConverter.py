# A simple script to convert amounts between different currencies

def currency_converter():
    # Example fixed exchange rates (relative to USD)
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "INR": 82.95,
        "JPY": 150.15
    }

    print("--- Simple Currency Converter ---")
    print("Available currencies: USD, EUR, GBP, INR, JPY")
    
    amount = float(input("Enter the amount: "))
    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()

    if from_currency in rates and to_currency in rates:
        # Convert to USD first, then to target currency
        amount_in_usd = amount / rates[from_currency]
        converted_amount = amount_in_usd * rates[to_currency]
        
        print(f"\n{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Sorry, one of the currencies is not supported yet.")

if __name__ == "__main__":
    currency_converter()