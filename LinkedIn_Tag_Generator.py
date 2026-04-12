# Practicing String Manipulation for Professional Branding

def generate_tags(topic):
    # Professional tag database
    tag_library = {
        "ai": ["#ArtificialIntelligence", "#MachineLearning", "#AI", "#DeepLearning"],
        "python": ["#PythonProgramming", "#Coding", "#Developer", "#100DaysOfCode"],
        "japan": ["#JapanCareers", "#WorkInJapan", "#TokyoIT", "#N5Study"]
    }
    
    # Japanese equivalents for professional reach
    japanese_tags = ["#エンジニア", "#プログラミング", "#AI開発", "#キャリア"]
    
    print(f"---  LinkedIn Tag Generator: {topic.upper()} ---")
    
    # 1. Logic to fetch and combine tags
    selected_tags = tag_library.get(topic.lower(), ["#Tech", "#Innovation"])
    
    # 2. String Joining
    eng_string = " ".join(selected_tags)
    jp_string = " ".join(japanese_tags)
    
    print(f"\nCopy these to your post:\n")
    print(f"{eng_string} {jp_string}")
    print("\n-------------------------------------------")

if __name__ == "__main__":
    user_topic = input("Enter topic (ai, python, or japan): ")
    generate_tags(user_topic)