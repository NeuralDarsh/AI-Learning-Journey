# Practicing Project Management logic and array status filtering in Python

def run_migration_scheduler():
    print("==================================================")
    print("JAPAN RELOCATION MILESTONE SCHEDULER")
    print("==================================================")
    
    # 1. Project Tasks Database (Task Name, Status)
    # False = Pending, True = Completed
    project_tasks = {
        "Complete 4th-Semester Exams": True,
        "Master JLPT N5 Vocabulary & Grammar": False,
        "Build 3 Major AI/ML Projects on GitHub": True,
        "Optimize LinkedIn Profile for Tokyo Recruiters": True,
        "Apply for Passport and Work Visa Verification": False
    }
    
    # 2. Filter tasks using list comprehensions (Project Management Status)
    completed_tasks = [task for task, status in project_tasks.items() if status]
    pending_tasks = [task for task, status in project_tasks.items() if not status]
    
    total_tasks = len(project_tasks)
    completion_rate = (len(completed_tasks) / total_tasks) * 100
    
    # 3. Display Project Status Report
    print(f"Overall Project Completion Rate: {completion_rate:.1f}%\n")
    
    print(" COMPLETED MILESTONES:")
    for task in completed_tasks:
        print(f"  [X] {task}")
        
    print("\n PENDING MILESTONES (Critical Path):")
    for task in pending_tasks:
        print(f"  [ ] {task}")
        
    print("==================================================")
    print(" PM Tip: Focus heavily on the language blocks next!")
    print("==================================================")

if __name__ == "__main__":
    run_migration_scheduler()