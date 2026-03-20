# Understanding O(n) Time Complexity and Search Logic

import time

def linear_search(data_list, target):
    print(f"--- 🔍 Starting Search for Target: {target} ---")
    print(f"Dataset: {data_list}\n")
    
    for index in range(len(data_list)):
        current_value = data_list[index]
        print(f"Step {index + 1}: Checking index {index} (Value: {current_value})...", end=" ")
        
        time.sleep(0.5) # Adding a delay to simulate 'thinking'
        
        if current_value == target:
            print(" FOUND!")
            return index
        else:
            print(" Not a match.")
            
    return -1

if __name__ == "__main__":
    # A list of numbers (could be IDs, ages, or sensor readings)
    my_numbers = [12, 45, 67, 23, 89, 34, 56, 90]
    
    goal = int(input("Enter a number to find in the list: "))
    
    result = linear_search(my_numbers, goal)
    
    if result != -1:
        print(f"\nTarget found at Index: {result}")
    else:
        print("\nTarget was not found in the list.")