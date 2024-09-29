# Arrays and Matrices
class Array:
    def __init__(self):
        self.array = []

    # Insert element at the end
    def insert(self, element):
        self.array.append(element)

    # Delete element at a specific index
    def delete(self, index):
        if index < len(self.array):
            return self.array.pop(index)
        else:
            return "Index out of range"

    # Access element at a specific index
    def access(self, index):
        if index < len(self.array):
            return self.array[index]
        else:
            return "Index out of range"

    # Display the array
    def display(self):
        return self.array


# Matrix Implementation
class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Insert value at a specific position
    def insert(self, row, col, value):
        self.matrix[row][col] = value

    # Access element at a specific position
    def access(self, row, col):
        return self.matrix[row][col]

    # Display the matrix
    def display(self):
        for row in self.matrix:
            print(row)


# Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []

    # Push an element to the stack
    def push(self, element):
        self.stack.append(element)

    # Pop the top element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    # Check the top element
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display the stack
    def display(self):
        return self.stack

# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue an element to the queue
    def enqueue(self, element):
        self.queue.append(element)

    # Dequeue an element from the front
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display the queue
    def display(self):
        return self.queue

# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert element at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        # If the head node itself holds the key
        if current is not None:
            if current.data == key:
                self.head = current.next
                current = None
                return

        # Search for the key to be deleted
        prev = None
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next

        # If the key is not present
        if current is None:
            return "Node not found"

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Rooted Trees Using Linked Lists

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    # Add a child node
    def add_child(self, child_node):
        self.children.append(child_node)

    # Display tree structure
    def display(self, level=0):
        print(" " * level + str(self.value))
        for child in self.children:
            child.display(level + 2)

# Example of using rooted tree
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.add_child(child1)
root.add_child(child2)

child1.add_child(TreeNode(4))
child1.add_child(TreeNode(5))
child2.add_child(TreeNode(6))

root.display()
