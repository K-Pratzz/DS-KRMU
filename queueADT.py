queue = []

def insert():
    item = int(input("Enter element to insert: "))
    queue.append(item)
    print(item, "inserted into queue")

def delete():
    if len(queue) == 0:
        print("Queue is empty, cannot delete")
    else:
        removed_item = queue.pop(0)
        
        # Display the deleted element
        print(removed_item, "deleted from queue")

def traversal():
    # Check if queue is empty
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements are:")
        
        # for loop is used to go through each element in queue
        for element in queue:
            # Print each element one by one
            print(element)

while True:
    # Display menu options
    print("\nQueue Operations")
    print("1. Insert")
    print("2. Delete")
    print("3. Traversal")
    print("4. Exit")
    
    # Take user choice
    choice = int(input("Enter your choice: "))
    
    # If user chooses 1, call insert function
    if choice == 1:
        insert()
    
    # If user chooses 2, call delete function
    elif choice == 2:
        delete()
    
    # If user chooses 3, call traversal function
    elif choice == 3:
        traversal()
    
    # If user chooses 4, exit the program
    elif choice == 4:
        print("Exiting program")
        break
    
    # If user enters wrong option
    else:
        print("Invalid choice, please try again")