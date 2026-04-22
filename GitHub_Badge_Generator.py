# Practicing String Formatting and URL Encoding for Documentation

def generate_badge():
    print("---  GitHub README Badge Generator ---")
    print("Powered by Shields.io logic\n")
    
    # 1. Collect Badge Information
    label = input("Enter Label (e.g., Python, N5_Japanese, IoT): ").strip()
    message = input("Enter Status/Message (e.g., Active, Learning, 4th_Sem): ").strip()
    color = input("Enter Color (e.g., blue, green, orange, brightgreen): ").strip()

    label_url = label.replace(" ", "%20")
    message_url = message.replace(" ", "%20")

    # Format: ![Label](https://img.shields.io/badge/Label-Message-Color)
    badge_markdown = f"![{label}](https://img.shields.io/badge/{label_url}-{message_url}-{color})"

    print("\n Your Markdown Badge Code:")
    print("-" * 30)
    print(badge_markdown)
    print("-" * 30)
    print("\nExample Preview Logic: " + label + " | " + message)

if __name__ == "__main__":
    generate_badge()