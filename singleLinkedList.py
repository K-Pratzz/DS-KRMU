# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # INSERT (always adds at end)
    def insert(self, data):
        new_node = Node(data) #object of node class

        # if list empty
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next #stores the address of 

        temp.next = new_node #

    # DELETE (by value)
    def delete(self, value):
        temp = self.head
        prev = None

        # deleting head
        if temp and temp.data == value: 
            self.head = temp.next
            return

        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    # TRAVERSE (display list)
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# ----------- DRIVER CODE -----------

ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Linked List:")
ll.traverse()

ll.delete(20)

print("After Deletion:")
ll.traverse()