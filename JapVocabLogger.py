# Learning File I/O: Reading and Writing to external files

def add_vocab():
    word = input("Enter Japanese Word (e.g., Sakura): ")
    meaning = input("Enter English Meaning: ")
    
    # 'a' stands for 'append' - it adds to the file without deleting old data
    with open("my_vocab.txt", "a", encoding="utf-8") as file:
        file.write(f"{word} : {meaning}\n")
    
    print(f"Successfully saved '{word}' to my_vocab.txt!")

def view_vocab():
    print("\n--- Your Saved Vocabulary ---")
    try:
        with open("my_vocab.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print(content if content else "The file is empty.")
    except FileNotFoundError:
        print("No vocabulary file found yet. Add a word first!")

if __name__ == "__main__":
    print("--- 🇯🇵 N5 Study Logger 🇯🇵 ---")
    choice = input("Do you want to (A)dd a word or (V)iew all? ").upper()
    
    if choice == "A":
        add_vocab()
    elif choice == "V":
        view_vocab()
    else:
        print("Invalid choice.")