# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ---------------- LINKED LIST CLASS ----------------
class LinkedList:
    def __init__(self):
        self.head = None


    # -------- INSERT AT END --------
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    # -------- INSERT AT BEGINNING --------
    def insert_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    # -------- INSERT AT POSITION --------
    def insert_at_position(self, value, pos):
        new_node = Node(value)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    # -------- DELETE FIRST --------
    def delete_begin(self):
        if self.head is None:
            print("List empty")
            return

        self.head = self.head.next


    # -------- DELETE LAST --------
    def delete_end(self):
        if self.head is None:
            print("List empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None


    # -------- DELETE BY VALUE --------
    def delete_value(self, value):
        if self.head is None:
            print("List empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found")


    # -------- SEARCH --------
    def search(self, value):
        temp = self.head
        pos = 1

        while temp:
            if temp.data == value:
                print("Found at position", pos)
                return
            temp = temp.next
            pos += 1

        print("Not found")


    # -------- TRAVERSAL --------
    def traversal(self):
        if self.head is None:
            print("List empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------------- MAIN MENU ----------------
ll = LinkedList()

while True:
    print("\n1.Insert End  2.Insert Begin  3.Insert Position")
    print("4.Delete Begin  5.Delete End  6.Delete Value")
    print("7.Search  8.Traversal  9.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        ll.insert_end(int(input("Value: ")))

    elif ch == 2:
        ll.insert_begin(int(input("Value: ")))

    elif ch == 3:
        val = int(input("Value: "))
        pos = int(input("Position: "))
        ll.insert_at_position(val, pos)

    elif ch == 4:
        ll.delete_begin()

    elif ch == 5:
        ll.delete_end()

    elif ch == 6:
        ll.delete_value(int(input("Value: ")))

    elif ch == 7:
        ll.search(int(input("Value: ")))

    elif ch == 8:
        ll.traversal()

    elif ch == 9:
        break

    else:
        print("Invalid choice")