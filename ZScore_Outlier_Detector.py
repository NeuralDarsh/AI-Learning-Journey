# Essential for Applied Statistics and Data Cleaning in AI

import numpy as np

def detect_outliers(data):
    print("---  Statistics: Z-Score Outlier Detection ---")
    
    # 1. Calculate Mean and Standard Deviation
    mean = np.mean(data)
    std = np.std(data)
    
    print(f"Dataset Mean: {mean:.2f}")
    print(f"Standard Deviation: {std:.2f}\n")
    
    threshold = 2 # In professional AI, we often use 3, but 2 is good for small samples
    outliers = []
    
    for x in data:
        # 2. Z-Score Formula: (Value - Mean) / StdDev
        z_score = (x - mean) / std
        
        if np.abs(z_score) > threshold:
            outliers.append(x)
            status = " OUTLIER"
        else:
            status = "Normal"
            
        print(f"Value: {x:<3} | Z-Score: {z_score:>6.2f} | {status}")
        
    return outliers

if __name__ == "__main__":
    # Example: Daily study minutes (90 is the outlier here)
    study_minutes = [30, 35, 28, 32, 31, 90, 29, 33]
    
    results = detect_outliers(study_minutes)
    print(f"\nDetected Outliers: {results}")