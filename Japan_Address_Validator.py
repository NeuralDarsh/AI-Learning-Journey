# Practicing Regular Expressions (Regex) and String Validation

import re

def validate_japanese_info():
    print("---  Japan Address & Postal Validator ---")
    
    # 1. Japanese Postal Code Pattern: 3 digits, hyphen, 4 digits (e.g., 100-0001)
    postal_pattern = r"^\d{3}-\d{4}$"
    
    postal_code = input("Enter Japanese Postal Code (Format: 000-0000): ")
    
    # 2. Validation Logic
    if re.match(postal_pattern, postal_code):
        print(f" '{postal_code}' is a valid Japanese postal code format.")
    else:
        print(f" '{postal_code}' is invalid. It must be 3 digits, a hyphen, then 4 digits.")

    # 3. Prefecture Check
    # Common prefectures you'll see in job listings
    prefectures = ["Tokyo", "Osaka", "Kyoto", "Kanagawa", "Fukuoka"]
    
    print("\n---  Major IT Hubs in Japan ---")
    city = input("Which city/prefecture are you targeting? ").capitalize().strip()
    
    if city in prefectures:
        print(f" {city} is a major tech hub! Great choice for an AI/ML career.")
    else:
        print(f" {city} is an interesting location to research for local opportunities.")

if __name__ == "__main__":
    validate_japanese_info()