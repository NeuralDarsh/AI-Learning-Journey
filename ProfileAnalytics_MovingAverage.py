# Practicing Data Smoothing and Moving Averages with NumPy

import numpy as np

def analyze_profile_trends(views_list):
    print("---  LinkedIn Profile Analytics: Trend Analysis ---")
    
    views = np.array(views_list)
    
    # 1. Calculate Simple Moving Average (Window of 3 days)
    # This helps see the trend by smoothing daily spikes
    weights = np.ones(3) / 3
    moving_avg = np.convolve(views, weights, mode='valid')
    
    print(f"Daily Views (Last 7 Days): {views_list}")
    print(f"\n3-Day Moving Averages:")
    
    for i, avg in enumerate(moving_avg):
        print(f"Period {i+1}: {avg:.2f} views/day")

    # 2. Growth Logic
    if moving_avg[-1] > moving_avg[0]:
        print("\n Trend: Your profile reach is GROWING. Keep posting!")
    else:
        print("\n Trend: Reach is stabilizing. Try engaging with more Japan-based recruiters.")

if __name__ == "__main__":
    # Example: Profile views over the last week
    daily_profile_views = [12, 15, 10, 25, 18, 22, 30]
    analyze_profile_trends(daily_profile_views)