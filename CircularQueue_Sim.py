# A core Data Structures concept used in IoT and Operating Systems

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, data):
        # Check if the queue is full
        if ((self.tail + 1) % self.size == self.head):
            print(" Queue is Full! Cannot add:", data)
        
        # If queue is empty
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
            print(f" Enqueued: {data}")
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data
            print(f" Enqueued: {data}")

    def dequeue(self):
        # Check if queue is empty
        if (self.head == -1):
            print(" Queue is Empty!")
        
        # If there's only one element
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            print(f" Dequeued: {temp}")
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            print(f" Dequeued: {temp}")
            return temp

    def display(self):
        if(self.head == -1):
            print("Queue is empty")
        elif (self.tail >= self.head):
            print("Current Queue:", end=" ")
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Current Queue:", end=" ")
            for i in range(self.head, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

if __name__ == "__main__":
    # Initialize a queue of size 5
    cq = CircularQueue(5)
    
    cq.enqueue("Temp_Data_1")
    cq.enqueue("Temp_Data_2")
    cq.enqueue("Temp_Data_3")
    cq.display()
    
    cq.dequeue()
    cq.display()
    
    cq.enqueue("Temp_Data_4")
    cq.enqueue("Temp_Data_5")
    cq.enqueue("Temp_Data_6") # This should trigger the circle logic
    cq.display()