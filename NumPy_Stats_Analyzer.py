# Calculating Variance and Standard Deviation (Measure of Spread)

import numpy as np

def calculate_spread():
    # Example: Your scores in 7 mock Japanese N5 vocabulary tests
    data = np.array([85, 88, 84, 90, 86, 87, 85])
    
    print("---  Applied Statistics: NumPy Analysis ---")
    print(f"Dataset (Test Scores): {data}")

    # 1. Mean (Average)
    mean_val = np.mean(data)
    
    # 2. Variance (Average of squared differences from the Mean)
    # In RDBMS/Stats, this is denoted as sigma squared
    variance_val = np.var(data)
    
    # 3. Standard Deviation (Square root of Variance)
    # This is the most common measure used in AI/ML
    std_dev_val = np.std(data)

    print(f"\nMean Score: {mean_val:.2f}")
    print(f"Variance: {variance_val:.2f}")
    print(f"Standard Deviation: {std_dev_val:.2f}")

    print("\n AI Tip: A low Std Dev means your scores are very stable!")

if __name__ == "__main__":
    calculate_spread()