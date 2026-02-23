# A script that sends a desktop notification to remind you of tasks

import time
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,  # You can add a path to an .ico file here
        timeout = 10      # Notification stays for 10 seconds
    )

if __name__ == "__main__":
    # Example: A reminder to drink water or take a break
    task_title = "Coding Break!"
    task_message = "You've been coding for a while. Stand up and stretch!"
    
    print("Notification sent!")
    send_notification(task_title, task_message)