# Practicing basic statistical data filtering and threshold logic

def detect_anomalies(data_stream, lower_bound, upper_bound):
    print("---  異常検知システム (IoT Anomaly Detection System) ---")
    print(f"Normal Range Configurations: {lower_bound}°C to {upper_bound}°C\n")
    
    clean_data = []
    anomalies_detected = []

    # 1. Parse the stream and separate clean data from outliers
    for reading in data_stream:
        if lower_bound <= reading <= upper_bound:
            clean_data.append(reading)
        else:
            anomalies_detected.append(reading)
            print(f"ALERT: Abnormal spike detected -> {reading}°C")

    # 2. Output statistics
    print("\n--- Processing Summary ---")
    print(f"Total Readings Processed: {len(data_stream)}")
    print(f"Valid Readings Saved:     {clean_data}")
    print(f"Anomalies Blocked:        {len(anomalies_detected)} detected")
    
    if anomalies_detected:
        print("Status: Maintenance check flagged due to sensor spikes.")
    else:
        print("Status: System stable. Data is fully clean.")

if __name__ == "__main__":
    # Simulated temperature reading stream containing realistic sensor noise spikes
    simulated_temperature_stream = [24.5, 25.1, 24.8, 99.9, 25.3, -12.4, 24.9]
    
    # Establish statistical guardrails for normal room temperature operations
    detect_anomalies(simulated_temperature_stream, lower_bound=15.0, upper_bound=35.0)