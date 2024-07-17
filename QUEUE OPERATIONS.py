class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue.pop(0)
        print(f"Dequeued: {item}")
        return item

    def size(self):
        return len(self.queue)

    def display(self):
        print(f"Queue: {self.queue}")

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    
    q.dequeue()
    q.display()
    
    q.dequeue()
    q.display()
    
    q.dequeue()
    q.display()
    
    q.dequeue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("The length of Queue: ", q.size())
