class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            print("Empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    def delete(self, key):
        if not self.head:
            return

        curr = self.head
        prev = None

        # Case: deleting head
        if curr.data == key:
            if curr.next == self.head:
                self.head = None
                return

            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            self.head = curr.next
            temp.next = self.head
            return

        # General case
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr.data == key:
                prev.next = curr.next
                return

        print("Value not found")