# Practicing Datetime management and Dictionary Lists

from datetime import datetime

def check_schedule():
    # 1. Content Queue: {Post Topic: Scheduled Hour (24h format)}
    content_queue = [
        {"topic": "Python Automation Tip", "hour": 9},
        {"topic": "IoT Project Update", "hour": 12},
        {"topic": "Learning Japanese N5 Kanji", "hour": 18},
        {"topic": "GitHub 100 Days Progress", "hour": 21}
    ]

    # 2. Get Current Hour
    current_hour = datetime.now().hour
    print(f"--- LinkedIn Scheduler Status (Current Hour: {current_hour}:00) ---")

    # 3. Logic to determine what to post
    posted_count = 0
    for post in content_queue:
        if current_hour >= post["hour"]:
            print(f" Published: {post['topic']} (Scheduled for {post['hour']}:00)")
            posted_count += 1
        else:
            print(f" Upcoming: {post['topic']} (Scheduled for {post['hour']}:00)")

    print(f"\nTotal posts live today: {posted_count}/{len(content_queue)}")

if __name__ == "__main__":
    check_schedule()