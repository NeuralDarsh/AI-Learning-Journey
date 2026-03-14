# Practice Engineering Physics formulas using Python's math module

import math

def calculate_circular_motion(radius, rpm):
    # Pi Day is the perfect time to use math.pi!
    pi_val = math.pi
    
    # 1. Calculate Circumference: 2 * pi * r
    circumference = 2 * pi_val * radius
    
    # 2. Convert RPM (Rotations Per Minute) to RPS (Per Second)
    rps = rpm / 60
    
    # 3. Linear Velocity (v = distance/time)
    velocity = circumference * rps
    
    return circumference, velocity

if __name__ == "__main__":
    print(f"--- Happy Pi Day (March 14)  ---")
    print("Concept: Circular Motion (Engineering Physics)\n")
    
    r = float(input("Enter radius of the circle (in meters): "))
    rotations = float(input("Enter RPM (Rotations per minute): "))
    
    c, v = calculate_circular_motion(r, rotations)
    
    print(f"\nResults:")
    print(f"Total Circumference: {c:.4f} m")
    print(f"Linear Velocity: {v:.4f} m/s")
    print(f"Using Pi value: {pi_val}")