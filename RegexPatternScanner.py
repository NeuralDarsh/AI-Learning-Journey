# Learning how to extract specific data (emails/phones) from messy text

import re

def scan_text(input_text):
    # Regex Patterns:
    # [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,} -> Standard Email Pattern
    # \+91\s\d{10} -> Indian Mobile Number Pattern (+91 1234567890)
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+91\s\d{10}'

    emails = re.findall(email_pattern, input_text)
    phones = re.findall(phone_pattern, input_text)

    return emails, phones

if __name__ == "__main__":
    # Simulating a messy block of text from a LinkedIn bio or contact page
    messy_data = """
    Contact me at darshan.ai@university.edu for collaborations. 
    You can also reach my office at +91 9876543210 or personal 
    email: contact@neuraldarsh.jp. Check my GitHub!
    """

    print("---  Regex Data Extraction Tool ---")
    e, p = scan_text(messy_data)

    print("\nEmails Found:")
    for email in e:
        print(f" {email}")

    print("\nPhone Numbers Found:")
    for phone in p:
        print(f" {phone}")