# Practicing Logic Building and Data Analysis

def analyze_streak(commit_data):
    total_commits = sum(commit_data)
    days_active = len([d for d in commit_data if d > 0])
    
    # Logic to find the longest consecutive streak of non-zero days
    max_streak = 0
    current_streak = 0
    
    for day in commit_data:
        if day > 0:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
            
    return total_commits, days_active, max_streak

if __name__ == "__main__":
    # Example: Commits per day for the last 14 days
    # (Imagine these are pulled from your NeuralDarsh profile)
    my_commits = [1, 3, 0, 2, 4, 1, 1, 0, 1, 2, 3, 1, 1, 5]
    
    total, active, streak = analyze_streak(my_commits)
    
    print("---  GitHub Profile: Streak Analyzer ---")
    print(f"Total Commits (Last 14 days): {total}")
    print(f"Days with Activity: {active} out of {len(my_commits)}")
    print(f" Longest Consecutive Streak: {streak} Days")
    
    # Career Goal Check
    if streak >= 7:
        print("\n Status: Highly Consistent! (Japanese recruiters love this).")
    else:
        print("\n Tip: Try to push at least one small change daily to keep the streak.")