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

    def peek(self):
        if self.is_empty():
            print("Queue is empty. No element to peek.")
            return None
        print(f"Peek: {self.queue[0]}")
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def display(self):
        print(f"Queue: {self.queue}")

if __name__ == "__main__":
    q = Queue()
    while True:
        print("\nOptions:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Peek")
        print("5. Display Size")
        print("6. Exit")
        
        choice = input("Choose an option (1/2/3/4/5/6): ")
        
        if choice == '1':
            item = input("Enter item to enqueue: ")
            q.enqueue(item)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.display()
        elif choice == '4':
            q.peek()
        elif choice == '5':
            print(f"Queue size: {q.size()}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
    
    print("The length of Queue: ", q.size())
