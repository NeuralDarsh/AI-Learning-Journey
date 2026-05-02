# Practicing Data Preprocessing for AI & ML

import numpy as np

def normalize_sensor_data(data):
    # 1. Min-Max Scaling Formula: (x - min) / (max - min)
    data_min = np.min(data)
    data_max = np.max(data)
    
    # Avoid division by zero if all values are the same
    if data_max == data_min:
        return np.zeros(data.shape)
        
    normalized = (data - data_min) / (data_max - data_min)
    return normalized

def main():
    print("---  IoT Data Normalizer for AI/ML ---")
    
    # Simulated raw sensor readings (e.g., Light Intensity 0-1023)
    raw_readings = np.array([120, 450, 890, 300, 750, 1000, 50])
    
    print(f"Raw Readings: {raw_readings}")
    
    # 2. Normalize the data
    scaled_data = normalize_sensor_data(raw_readings)
    
    print("\n---  Normalized Results (Range 0 to 1) ---")
    # Using a list comprehension to format the output nicely
    formatted_data = [round(val, 4) for val in scaled_data]
    print(formatted_data)

if __name__ == "__main__":
    main()