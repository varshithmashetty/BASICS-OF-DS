class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        n = Node(value)
        n.next = self.head
        if self.head != None:
            self.head.prev = n
        self.head = n

    def insert_at_tail(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = n
        n.prev = last

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__':
    dllist = DoublyLinkedList()
    dllist.insert_at_tail(1)
    dllist.insert_at_tail(2)
    dllist.insert_at_tail(3)
    dllist.insert_at_tail(4)
    dllist.insert_at_tail(5)
    print("After insertion at tail: ")
    dllist.display()
    dllist.insert_at_head(0)
    print("\nAfter insertion at head: ")
    dllist.display()
