# ---------------- List ADT using Array ----------------

class ArrayList:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)

    def display(self):
        print("Array List:", self.data)


# ---------------- List ADT using Linked List ----------------

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        print("Linked List:", end=" ")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# ---------------- Testing Both Implementations ----------------

arr = ArrayList()
arr.insert(10)
arr.insert(20)
arr.insert(30)
arr.display()

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()
