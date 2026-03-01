# Uses Dictionary Comprehension to convert names into phonetic code

def convert_to_nato():
    # The NATO Phonetic Alphabet Dictionary
    nato_dict = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
    }

    user_input = input("Enter a word to convert: ").upper()
    
    # Dictionary/List Comprehension - core logic
    try:
        result = [nato_dict[letter] for letter in user_input if letter != " "]
        print(f"\nPhonetic Code: {' - '.join(result)}")
    except KeyError:
        print("Please enter only alphabets (no numbers or symbols).")

if __name__ == "__main__":
    print("--- NATO Phonetic Alphabet Tool ---")
    convert_to_nato()