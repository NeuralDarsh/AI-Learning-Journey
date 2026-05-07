# Practicing Error Correction Logic and Function-based Data Scaling

def calibrate_sensor(raw_value, offset):
    """
    Adjusts the raw sensor reading by a known error offset.
    Formula: Corrected Value = Raw Value - Offset
    """
    return round(raw_value - offset, 2)

def run_calibration_demo():
    print("---  IoT Sensor Calibration & Offset Tool ---")
    
    # 1. Configuration: Known error for this specific device
    # (e.g., this sensor always reads 2.5 units too high)
    ERROR_OFFSET = 2.5
    
    # 2. Simulated Raw Readings from a faulty sensor
    raw_readings = [28.5, 30.1, 27.8, 31.0, 29.4]
    
    print(f"Correction Offset: -{ERROR_OFFSET} units")
    print("-" * 35)
    print(f"{'Raw Value':<12} | {'Calibrated':<12}")
    print("-" * 35)

    # 3. Processing the data
    for val in raw_readings:
        corrected = calibrate_sensor(val, ERROR_OFFSET)
        print(f"{val:<12} | {corrected:<12}")

    print("-" * 35)
    print(" Calibration complete. Data ready for AI processing.")

if __name__ == "__main__":
    run_calibration_demo()