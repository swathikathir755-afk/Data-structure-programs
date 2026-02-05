# ---------- Node Class ----------
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# ---------- Stack Using Linked List ----------
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        print("Popped:", self.top.data)
        self.top = self.top.next

    def display(self):
        temp = self.top
        print("Stack:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------- Testing Stack ----------
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()

# ---------- Queue Using Linked List ----------
class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def dequeue(self):
        if self.front_node is None:
            print("Queue Underflow")
            return
        print("Dequeued:", self.front_node.data)
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None

    def display(self):
        temp = self.front_node
        print("Queue:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------- Testing Queue ----------
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
queue.dequeue()
queue.display()
