# Essential for AI/ML Time-Series Data Processing

def calculate_moving_average(data, window_size):
    moving_averages = []
    
    # We loop through the data, but stop when there isn't enough left for a full window
    for i in range(len(data) - window_size + 1):
        # Extract the current window
        window = data[i : i + window_size]
        
        # Calculate the average of this window
        window_average = sum(window) / window_size
        moving_averages.append(round(window_average, 2))
        
    return moving_averages

if __name__ == "__main__":
    # Example: 10 days of temperature or stock prices
    raw_data = [22, 24, 21, 25, 28, 26, 30, 29, 31, 35]
    window = 3 # Calculating a 3-day moving average
    
    print("--- Data Science: Moving Average ---")
    print(f"Original Data: {raw_data}")
    
    averages = calculate_moving_average(raw_data, window)
    
    print(f"\n{window}-Day Moving Average Results:")
    print(averages)
    
    print("\nNote: Notice how the jumpy numbers become a smoother sequence!")