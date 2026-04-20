# Practicing Arithmetic Operations and Conditional Logic for Analytics

def calculate_engagement():
    print("---  LinkedIn Post Performance Analytics ---")
    
    try:
        # 1. Collect Post Data
        impressions = int(input("Enter total impressions (views): "))
        likes = int(input("Enter number of likes: "))
        comments = int(input("Enter number of comments: "))
        shares = int(input("Enter number of shares: "))

        if impressions == 0:
            print(" Impressions cannot be zero.")
            return

        # 2. Calculation: (Interactions / Impressions) * 100
        total_interactions = likes + comments + shares
        engagement_ratio = (total_interactions / impressions) * 100

        print(f"\n---  Results ---")
        print(f"Total Interactions: {total_interactions}")
        print(f"Engagement Ratio: {engagement_ratio:.2f}%")

        # 3. Performance Logic (Recruiter Reach Benchmarks)
        if engagement_ratio >= 5:
            status = " Viral/Excellent: Strong recruiter visibility!"
        elif engagement_ratio >= 2:
            status = " Good: Consistent professional reach."
        else:
            status = " Tip: Try adding more Japanese keywords to boost engagement."

        print(f"Performance: {status}")

    except ValueError:
        print(" Error: Please enter numerical values only.")

if __name__ == "__main__":
    calculate_engagement()