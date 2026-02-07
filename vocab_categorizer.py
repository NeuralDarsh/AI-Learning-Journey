# Concept: Modular Functions & Documentation

def categorize_words(word_list):
    """
    Takes a list of Japanese words and categorizes them by length.
    This mimics how AI models cluster text data.
    """
    short_words = []
    long_words = []

    for word in word_list:
        if len(word) <= 3:
            short_words.append(word)
        else:
            long_words.append(word)
            
    return short_words, long_words

def main():
    # A list of N5 vocabulary (4th Sem concept: Lists)
    my_vocab = ["Neko", "Mizu", "Taberu", "Sushi", "Inu", "Nihongo"]
    
    short, long = categorize_words(my_vocab)
    
    print("--- 📝 Japanese Vocab Clusters ---")
    print(f"Short Words (Easy): {short}")
    print(f"Long Words (Advanced): {long}")

if __name__ == "__main__":
    main()