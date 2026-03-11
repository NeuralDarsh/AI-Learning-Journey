# Calculating Mean, Median, and Mode from scratch in Python

from collections import Counter

def analyze_stats(data):
    # 1. Mean (Average)
    mean = sum(data) / len(data)

    # 2. Median (Middle Value)
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]

    # 3. Mode (Most Frequent)
    occurence = Counter(data)
    mode = occurence.most_common(1)[0][0]

    return mean, median, mode

if __name__ == "__main__":
    # Example: Test scores or Sensor data readings
    sample_data = [85, 90, 78, 90, 92, 88, 78, 90]
    
    print("--- 📊 Applied Statistics: Analyzer ---")
    print(f"Dataset: {sample_data}")
    
    avg, mid, freq = analyze_stats(sample_data)
    
    print(f"\nMean (Average): {avg}")
    print(f"Median (Middle): {mid}")
    print(f"Mode (Most Frequent): {freq}")