# Understanding the relationship between two variables in AI/ML

import math

def calculate_correlation(x, y):
    n = len(x)
    if n != len(y):
        return "Error: Lists must be the same length."

    # 1. Calculate Sums
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(i**2 for i in x)
    sum_y_sq = sum(i**2 for i in y)
    sum_xy = sum(x[i] * y[i] for i in range(n))

    # 2. Pearson Formula (Numerator and Denominator)
    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = math.sqrt((n * sum_x_sq - sum_x**2) * (n * sum_y_sq - sum_y**2))

    if denominator == 0:
        return 0
    
    return numerator / denominator

if __name__ == "__main__":
    # Example Data: [Hours Studied] vs [Exam Score]
    hours = [2, 3, 4, 5, 6, 7, 8]
    scores = [50, 55, 65, 70, 75, 85, 90]

    print("--- Statistics: Correlation Calculator ---")
    correlation = calculate_correlation(hours, scores)
    
    print(f"Dataset X (Hours): {hours}")
    print(f"Dataset Y (Scores): {scores}")
    print(f"\nCorrelation Coefficient: {correlation:.4f}")

    if correlation > 0.8:
        print("Interpretation: Strong Positive Correlation! ")
    elif correlation < -0.8:
        print("Interpretation: Strong Negative Correlation! ")
    else:
        print("Interpretation: Weak or No Correlation.")