# Simulating a Browser History "Back" Button

class BrowserHistory:
    def __init__(self):
        self.history = []

    def visit_page(self, url):
        print(f"Visiting: {url}")
        self.history.append(url) # This is 'PUSH' in Data Structures

    def go_back(self):
        if len(self.history) > 1:
            removed_page = self.history.pop() # This is 'POP' in Data Structures
            print(f"\n Moving back from: {removed_page}")
            print(f"Current Page: {self.history[-1]}")
        else:
            print("\n No more pages in history!")

if __name__ == "__main__":
    my_browser = BrowserHistory()
    
    print("---  Browser History (Stack) Simulator ---")
    my_browser.visit_page("google.com")
    my_browser.visit_page("github.com/NeuralDarsh")
    my_browser.visit_page("linkedin.com")

    # Show the stack status
    print(f"\nCurrent Stack: {my_browser.history}")

    # Simulate hitting the 'Back' button twice
    my_browser.go_back()
    my_browser.go_back()