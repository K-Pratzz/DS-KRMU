from collections import deque

queue = deque()

# -------- INSERT --------
def insert():
    item = int(input("Enter element to insert: "))
    queue.append(item)
    print(item, "inserted into queue")


# -------- DELETE --------
def delete():
    if not queue:
        print("Queue is empty")
    else:
        removed = queue.popleft()
        print(removed, "deleted from queue")


# -------- TRAVERSAL --------
def traversal():
    if not queue:
        print("Queue is empty")
    else:
        print("Queue elements:")
        for i in queue:
            print(i, end=" ")
        print()


# -------- PEEK --------
def peek():
    if not queue:
        print("Queue is empty")
    else:
        print("Front element:", queue[0])


# -------- MAIN --------
while True:
    print("\n1.Insert  2.Delete  3.Traversal  4.Peek  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        insert()
    elif ch == 2:
        delete()
    elif ch == 3:
        traversal()
    elif ch == 4:
        peek()
    elif ch == 5:
        break
    else:
        print("Invalid choice")