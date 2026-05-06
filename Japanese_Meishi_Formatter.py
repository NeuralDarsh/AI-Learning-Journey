# Practicing precise string alignment and layout design

def generate_meishi():
    # 1. Professional Data
    university = "D.Y. Patil Agri. & Tech. University" #
    major = "B.Tech in AI & ML (4th Sem)" #
    name_en = "Darshan Chidanand Bagale" #
    name_jp = "ダルシャン・バガレ" # Katakana version of your name
    email = "darshan.example@email.com"
    goal = "Future Software Engineer in Japan" #

    # 2. Design Settings
    width = 50
    border = "+" + "-" * (width - 2) + "+"

    # 3. Formatting Logic
    print("\n---  Your Digital Japanese Business Card ---")
    print(border)
    print(f"| {university.center(width-4)} |")
    print(f"| {major.center(width-4)} |")
    print(f"| {' ' * (width-4)} |")
    print(f"| {name_jp.center(width-4)} |") # Focus on Japanese name
    print(f"| {name_en.center(width-4)} |")
    print(f"| {' ' * (width-4)} |")
    print(f"| {email.center(width-4)} |")
    print(f"| {goal.center(width-4)} |")
    print(border)

if __name__ == "__main__":
    generate_meishi()