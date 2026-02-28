class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        # Initialize head and tail to None
        self.head = None
        self.tail = None

    def enqueue(self, x): #adding to the last 
        """Adds an element to the rear of the queue in O(1)."""
        new_node = Node(x)
        # If queue is empty, both head and tail point to new node
        if self.tail is None:
            self.head = self.tail = new_node
            return
        # Link the new node at the end and update tail
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self): #removing from the front
        """Removes the front element and handles underflow safely."""
        if self.is_empty():
            print("Queue Underflow: Cannot dequeue from an empty queue.")
            return None
        
        # Move head to the next node
        removed_data = self.head.data
        self.head = self.head.next
        
        # If head becomes None, tail must also be None
        if self.head is None:
            self.tail = None
            
        return removed_data

    def get_front(self):
        """Returns the front element without removing it."""
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("Front -> " + " -> ".join(elements) + " <- Rear" if elements else "Queue is Empty")

# --- Testing the Implementation ---
q = Queue()

print("Operations Sequence:")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print(f"Front element: {q.get_front()}")

print(f"Removed: {q.dequeue()}")
q.display()

print(f"Removed: {q.dequeue()}")
q.display()

print(f"Final State (is empty?): {q.is_empty()}")