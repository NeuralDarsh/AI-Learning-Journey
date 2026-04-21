# Practicing Linear Scaling and Value Mapping logic

def map_value(x, in_min, in_max, out_min, out_max):
    # 1. Linear Mapping Formula
    # This is essentially the equation of a line: y = mx + c
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def sensor_demo():
    print("--- IoT Sensor Range Mapper ---")
    
    # Example: Raw analog sensor input (0-1023) to Humidity % (0-100)
    try:
        raw_val = float(input("Enter raw sensor value (0-1023): "))
        
        if 0 <= raw_val <= 1023:
            # 2. Convert raw data to human-readable percentage
            percentage = map_value(raw_val, 0, 1023, 0, 100)
            
            # 3. Convert raw data to Voltage (for electronics debugging)
            voltage = map_value(raw_val, 0, 1023, 0, 5)
            
            print(f"\n---  Mapped Results ---")
            print(f"Percentage: {percentage:.2f}%")
            print(f"Voltage:    {voltage:.2f}V")
        else:
            print(" Error: Value must be between 0 and 1023.")
            
    except ValueError:
        print(" Error: Please enter a valid number.")

if __name__ == "__main__":
    sensor_demo()