import time

print("--- AI Career Initializer ---")
name = input("Enter your name: ")

print(f"Hello, {name}! Analyzing your B.Tech journey...")
time.sleep(2)

print("\n[ANALYSIS COMPLETE]")
print(f"Goal: Work in Japan (日本で働く)") # Added Japanese translation here
print(f"Status: Day 2 of GitHub")

# This is a 'Dictionary' - it maps English keys to Japanese values
translations = {
    "Python": "パイソン",
    "Machine Learning": "機械学習 (Kikai Gakushū)",
    "Neural Networks": "ニューラルネットワーク",
    "Japanese N5": "日本語 N5"
}

print("\nYour Roadmap (ロードマップ):")
for english, japanese in translations.items():
    # This line prints both languages side-by-side
    print(f"- {english} | {japanese}")

print("\nGanbatte, Darshan-san! (がんばって！)")