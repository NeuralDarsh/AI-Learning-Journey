# Celebrating March 3 with Object-Oriented Programming (OOP)

class HinaDoll:
    def __init__(self, name, rank, role):
        self.name = name
        self.rank = rank  # Tier level (1-7)
        self.role = role

    def display_info(self):
        print(f"Tier {self.rank}: {self.name} - ({self.role})")

def setup_festival():
    # Creating a list of Doll objects
    doll_collection = [
        HinaDoll("Odairi-sama", 1, "Emperor"),
        HinaDoll("Ohina-sama", 1, "Empress"),
        HinaDoll("Sannin Kanjo", 2, "Three Court Ladies"),
        HinaDoll("Gonin Bayashi", 3, "Five Musicians")
    ]

    print("--- 🎎 Hinamatsuri Tiered Display 🎎 ---")
    print("Happy Doll Festival & Holika Dahan!\n")
    
    # Sorting dolls by tier and displaying them
    for doll in doll_collection:
        doll.display_info()

if __name__ == "__main__":
    setup_festival()