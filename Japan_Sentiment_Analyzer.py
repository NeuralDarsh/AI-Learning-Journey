# Practicing String Parsing and Dictionary Mapping for AI/ML Text Data

def analyze_sentiment(text):
  
    lexicon = {
        "上手": 1,      # Jōzu (Skillful / Good at)
        "素晴らしい": 1, # Subarashii (Wonderful)
        "成功": 1,      # Seikō (Success)
        "問題": -1,     # Mondai (Problem / Issue)
        "失敗": -1,     # Shippai (Failure)
        "難しい": -1     # Muzukashii (Difficult)
    }
    
    score = 0
  
    for word, value in lexicon.items():
        if word in text:
            score += value
            
    # 3. Determine sentiment state
    if score > 0:
        return " POSITIVE (ポジティブ)"
    elif score < 0:
        return " NEGATIVE (ネガティブ)"
    else:
        return " NEUTRAL (ニュートラル)"

def run_analyzer():
    print("---  Japanese Text Sentiment Analyzer ---")
    
    # Simulated interview feedback or project review
    sample_text = "彼のPythonプログラミングは上手ですが、IoTの設計は少し難しいです。"
    # Translation: "His Python programming is good, but the IoT design is a bit difficult."
    
    print(f"Target Text: {sample_text}")
    result = analyze_sentiment(sample_text)
    print(f"Analysis Result: {result}")

if __name__ == "__main__":
    run_analyzer()