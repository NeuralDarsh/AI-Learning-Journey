# Simulating a Printer Queue or a Customer Service Line

class TaskQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        # Adding an item to the end of the line
        print(f" Adding Task: {task}")
        self.queue.append(task)

    def dequeue(self):
        # Removing the FIRST item that entered the line
        if len(self.queue) > 0:
            removed_task = self.queue.pop(0)
            print(f" Processing & Removing Task: {removed_task}")
        else:
            print(" Queue is empty! No tasks to process.")

    def display_status(self):
        print(f"Current Queue: {self.queue}")

if __name__ == "__main__":
    print("---  Printer Queue (FIFO) Simulator ---")
    my_printer = TaskQueue()

    # Adding tasks (Enqueue)
    my_printer.enqueue("Japanese_N5_Notes.pdf")
    my_printer.enqueue("AI_Project_Report.docx")
    my_printer.enqueue("Holi_Photos.jpg")

    my_printer.display_status()

    # Processing tasks (Dequeue)
    # Notice how the PDF (the first one in) is the first one out!
    my_printer.dequeue()
    my_printer.display_status()
    
    my_printer.dequeue()
    my_printer.display_status()