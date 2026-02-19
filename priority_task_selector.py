import random

def get_weighted_task(task_map):
    """
    Selects a task based on assigned probability weights.
    """
    tasks = list(task_map.keys())
    weights = list(task_map.values())
    
    # random.choices returns a list, so we take the first element [0]
    selection = random.choices(tasks, weights=weights, k=1)[0]
    return selection

def main():
    print("--- Daily AI Learning Goal Selector ---")
    
    # Task : Weight (Higher weight = higher chance of being picked)
    my_tasks = {
        "N5 Kanji Practice": 30,
        "AI/ML Model Logic (Zoho Training)": 40,
        "Instagram Content (nippon.addict)": 10
    }
    
    selected = get_weighted_task(my_tasks)
    
    print(f"\nToday's Priority Focus: {selected}")
    print(f"Confidence Level: {my_tasks[selected]}%")

if __name__ == "__main__":
    main()