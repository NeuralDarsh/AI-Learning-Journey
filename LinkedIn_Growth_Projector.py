# Practicing Linear Forecasting and Milestone Logic

def project_growth(current_followers, weekly_growth):
    print("---  LinkedIn Network Growth Projector ---")
    print(f"Current Followers: {current_followers}")
    print(f"Weekly Growth Rate: +{weekly_growth} followers/week\n")

    milestones = [500, 1000, 2000]
    
    # 1. Projecting milestones
    for target in milestones:
        if current_followers >= target:
            continue
            
        # 2. Formula: (Target - Current) / Weekly Rate
        weeks_needed = (target - current_followers) / weekly_growth
        months_needed = weeks_needed / 4.34  # Average weeks in a month
        
        print(f" Milestone: {target} Followers")
        print(f"   Estimated Time: {int(weeks_needed)} weeks (~{months_needed:.1f} months)")
        print(f"   Target Date: Week {int(weeks_needed)} from now\n")

    print(" Strategy: To reach Japan-based recruiters faster, increase daily engagement!")

if __name__ == "__main__":
    # Example: Starting with 320 followers, growing by 15 per week
    project_growth(current_followers=320, weekly_growth=15)