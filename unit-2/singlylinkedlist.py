# Creating a class named Node
# class → used to create user-defined data type
# Node → name of the class
class Node:
    
    # __init__ → constructor function
    # self → reference to current object
    # data → value stored in node
    def __init__(self, data):
        
        # self.data → variable to store data in node
        self.data = data
        
        # self.next → pointer to next node
        # None → means no next node (null)
        self.next = None


# Creating a class for Linked List
class LinkedList:
    
    # Constructor for LinkedList
    def __init__(self):
        
        # self.head → stores address of first node
        # Initially list is empty, so head is None
        self.head = None


    # Function to insert a new node at the end
    def insert(self, data):
        
        # Create a new node using Node class
        new_node = Node(data)
        
        # If linked list is empty
        if self.head is None:
            
            # Make new node as first node
            self.head = new_node
            return
        
        # temp → temporary variable to traverse list
        temp = self.head
        
        # while → loop runs until condition is False
        # temp.next != None → move until last node
        while temp.next is not None:
            temp = temp.next
        
        # Connect last node to new node
        temp.next = new_node


    # Function to display all elements (Traversal)
    def traverse(self):
        
        # temp starts from head node
        temp = self.head
        
        # If list is empty
        if temp is None:
            print("Linked List is empty")
            return
        
        # Loop through linked list
        while temp is not None:
            
            # Print data of current node
            print(temp.data, end=" -> ")
            
            # Move to next node
            temp = temp.next
        
        # Print None at end of list
        print("None")


    # Function to search an element
    def search(self, key):
        
        # temp starts from head
        temp = self.head
        
        # position → keeps track of node number
        position = 1
        
        # Loop until end of list
        while temp is not None:
            
            # If data matches key
            if temp.data == key:
                print(f"Element {key} found at position {position}")
                return
            
            # Move to next node
            temp = temp.next
            position += 1
        
        # If element not found
        print(f"Element {key} not found in linked list")


# Creating object of LinkedList class
ll = LinkedList()

# Inserting elements
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

# Traversing linked list
print("Linked List elements:")
ll.traverse()

# Searching elements
ll.search(30)
ll.search(50)