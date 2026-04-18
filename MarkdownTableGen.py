# Automating GitHub README documentation using Python String Formatting

def generate_markdown_table():
    print("---  GitHub README Table Generator ---")
    
    projects = []
    
    # 1. Collect data for the table
    while True:
        day = input("\nEnter Day Number (or 'exit' to finish): ")
        if day.lower() == 'exit': break
        
        eng_desc = input("Enter English Description: ")
        jp_desc = input("Enter Japanese Description: ")
        
        projects.append([day, eng_desc, jp_desc])

    # 2. Generate the Markdown Header
    header = "| Day | Project Description (English) | プロジェクトの説明 (Japanese) |\n"
    separator = "| :--- | :--- | :--- |\n"
    
    # 3. Generate Rows with f-string alignment
    rows = ""
    for p in projects:
        rows += f"| {p[0]} | {p[1]} | {p[2]} |\n"

    final_table = header + separator + rows
    
    print("\n Your Markdown Table is ready to copy:\n")
    print(final_table)

if __name__ == "__main__":
    generate_markdown_table()