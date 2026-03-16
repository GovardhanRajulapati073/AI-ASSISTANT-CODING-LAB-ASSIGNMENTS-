#Lab 11 – Data Structures with AI: Implementing Fundamental Structures

#Task Description #1 – Stack Implementation
#Task: Use AI to generate a Stack class with push, pop, peek, and is_empty methods.
#Sample Input Code:
#class Stack:
#pass
#Expected Output:
#• A functional stack implementation with all required methods and docstrings.

class Stack:
    """
    A simple implementation of a Stack data structure (LIFO - Last In, First Out).
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Parameters:
        item : any
            The element to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the item from the top of the stack.
        
        Returns:
        any
            The element removed from the stack.
        
        Raises:
        IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the item at the top of the stack without removing it.
        
        Returns:
        any
            The element at the top of the stack.
        
        Raises:
        IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
        bool
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def __len__(self):
        """
        Return the number of items in the stack.
        
        Returns:
        int
            The size of the stack.
        """
        return len(self.items)

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())   # Output: 20
print(stack.pop())    # Output: 20
print(stack.is_empty())  # Output: False
print(len(stack))     # Output: 1







#Task Description #2 – Queue Implementation
#Task: Use AI to implement a Queue using Python lists.
#Sample Input Code:
#class Queue:
#pass
#Expected Output:
#• FIFO-based queue class with enqueue, dequeue, peek, and size methods.
class Queue:
    """
    A simple implementation of a Queue data structure (FIFO - First In, First Out).
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Parameters:
        item : any
            The element to be added to the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        
        Returns:
        any
            The element removed from the queue.
        
        Raises:
        IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """
        Return the item at the front of the queue without removing it.
        
        Returns:
        any
            The element at the front of the queue.
        
        Raises:
        IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def size(self):
        """
        Return the number of items in the queue.
        
        Returns:
        int
            The size of the queue.
        """
        return len(self.items)

    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
        bool
            True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.peek())     # Output: 10
print(queue.dequeue())  # Output: 10
print(queue.size())     # Output: 2
print(queue.is_empty()) # Output: False






#Task Description #3 – Linked List
#Task: Use AI to generate a Singly Linked List with insert and display methods.
#Sample Input Code:
#class Node:
#pass
#class LinkedList:
#pass
#Expected Output:
#• A working linked list implementation with clear method documentation.

class Node:
    """
    A Node in a singly linked list.
    """

    def __init__(self, data):
        """
        Initialize a node with data and a pointer to the next node.
        
        Parameters:
        data : any
            The value stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A simple implementation of a Singly Linked List.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def insert(self, data):
        """
        Insert a new node with the given data at the end of the list.
        
        Parameters:
        data : any
            The value to be inserted into the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse until the last node
                current = current.next
            current.next = new_node

    def display(self):
        """
        Display all elements in the linked list.
        
        Returns:
        str
            A string representation of the linked list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty List"
    
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
print(ll.display())  # Output: 10 -> 20 -> 30






#Task Description #4 – Binary Search Tree (BST)
#Task: Use AI to create a BST with insert and in-order traversal methods.
#Sample Input Code:
#class BST:
#pass
#Expected Output:
#• BST implementation with recursive insert and traversal methods.

class Node:
    """
    A Node in the Binary Search Tree.
    """

    def __init__(self, key):
        """
        Initialize a node with a key and left/right children.
        
        Parameters:
        key : int or comparable type
            The value stored in the node.
        """
        self.key = key
        self.left = None
        self.right = None


class BST:
    """
    A simple Binary Search Tree (BST) implementation.
    """

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, key):
        """
        Insert a new key into the BST.
        
        Parameters:
        key : int or comparable type
            The value to be inserted.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        """
        Helper method to recursively insert a key.
        """
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)
        # If key == current.key, we skip to avoid duplicates

    def in_order_traversal(self):
        """
        Perform in-order traversal of the BST.
        
        Returns:
        list
            A list of keys in sorted order.
        """
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, current, result):
        """
        Helper method to recursively perform in-order traversal.
        """
        if current:
            self._in_order_recursive(current.left, result)
            result.append(current.key)
            self._in_order_recursive(current.right, result)
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print(bst.in_order_traversal())  
# Output: [20, 30, 40, 50, 60, 70, 80]





#Task Description #5 – Hash Table
#Task: Use AI to implement a hash table with basic insert, search, and
#delete methods.
#Sample Input Code:
#class HashTable:
#pass
#Expected Output:
#• Collision handling using chaining, with well-commented methods.

class HashTable:
    """
    A simple Hash Table implementation using chaining for collision handling.
    """

    def __init__(self, size=10):
        """
        Initialize the hash table with a given size.
        
        Parameters:
        size : int
            The number of buckets in the hash table (default is 10).
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Generate a hash index for a given key.
        
        Parameters:
        key : any (hashable)
            The key to be hashed.
        
        Returns:
        int
            The index in the table where the key-value pair should be stored.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        
        Parameters:
        key : any (hashable)
            The key to be inserted.
        value : any
            The value associated with the key.
        """
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Insert new key-value pair

    def search(self, key):
        """
        Search for a value by key in the hash table.
        
        Parameters:
        key : any (hashable)
            The key to search for.
        
        Returns:
        any
            The value associated with the key, or None if not found.
        """
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        
        Parameters:
        key : any (hashable)
            The key to be deleted.
        
        Returns:
        bool
            True if the key was found and deleted, False otherwise.
        """
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def display(self):
        """
        Display the contents of the hash table.
        
        Returns:
        str
            A string representation of the hash table.
        """
        result = []
        for i, bucket in enumerate(self.table):
            result.append(f"Bucket {i}: {bucket}")
        return "\n".join(result)
    
ht = HashTable(size=5)
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("grape", 30)

print(ht.search("banana"))   # Output: 20
ht.delete("apple")
print(ht.search("apple"))    # Output: None

print(ht.display())
# Example Output:
# Bucket 0: []
# Bucket 1: [('banana', 20)]
# Bucket 2: []
# Bucket 3: [('grape', 30)]
# Bucket 4: []






#Task Description #6 – Graph Representation
#Task: Use AI to implement a graph using an adjacency list.
#Sample Input Code:
#class Graph:
#pass
#Expected Output:
#• Graph with methods to add vertices, add edges, and display connections.

class Graph:
    """
    A simple Graph implementation using an adjacency list.
    """

    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Add a new vertex to the graph.
        
        Parameters:
        vertex : any (hashable)
            The vertex to be added.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Add an edge between two vertices (undirected).
        
        Parameters:
        vertex1, vertex2 : any (hashable)
            The vertices to connect.
        """
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        # Add the edge (undirected graph)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def display(self):
        """
        Display the adjacency list of the graph.
        
        Returns:
        str
            A string representation of the graph connections.
        """
        result = []
        for vertex, neighbors in self.graph.items():
            result.append(f"{vertex} -> {', '.join(map(str, neighbors))}")
        return "\n".join(result)
    
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
print(g.display())






#Task Description #7 – Priority Queue
#Task: Use AI to implement a priority queue using Python’s heapq module.
#Sample Input Code:
#class PriorityQueue:
#pass
#Expected Output:
#• Implementation with enqueue (priority), dequeue (highest priority),and display methods.

import heapq

class PriorityQueue:
    """
    A Priority Queue implementation using Python's heapq module.
    Lower priority numbers indicate higher priority.
    """

    def __init__(self):
        """
        Initialize an empty priority queue.
        """
        self.queue = []

    def enqueue(self, priority, item):
        """
        Add an item to the queue with a given priority.
        
        Parameters:
        priority : int
            The priority of the item (lower value = higher priority).
        item : any
            The element to be added.
        """
        heapq.heappush(self.queue, (priority, item))

    def dequeue(self):
        """
        Remove and return the item with the highest priority.
        
        Returns:
        any
            The element with the highest priority.
        
        Raises:
        IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty priority queue")
        return heapq.heappop(self.queue)[1]

    def display(self):
        """
        Display the contents of the priority queue.
        
        Returns:
        str
            A string representation of the queue (sorted by priority).
        """
        return str(sorted(self.queue))

    def is_empty(self):
        """
        Check if the priority queue is empty.
        
        Returns:
        bool
            True if empty, False otherwise.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Return the number of items in the queue.
        
        Returns:
        int
            The size of the queue.
        """
        return len(self.queue)
    
pq = PriorityQueue()
pq.enqueue(2, "Task B")
pq.enqueue(1, "Task A")
pq.enqueue(3, "Task C")

print(pq.display())      # Output: [(1, 'Task A'), (2, 'Task B'), (3, 'Task C')]
print(pq.dequeue())      # Output: Task A (highest priority)
print(pq.size())         # Output: 2
print(pq.is_empty())     # Output: False







#Task Description #8 – Deque
#Task: Use AI to implement a double-ended queue using collections.deque.
#Sample Input Code:
#class DequeDS:
#pass
#Expected Output:
#• Insert and remove from both ends with docstrings.

from collections import deque

class DequeDS:
    """
    A Double-Ended Queue (Deque) implementation using collections.deque.
    Supports insertion and removal from both ends.
    """

    def __init__(self):
        """
        Initialize an empty deque.
        """
        self.deque = deque()

    def insert_front(self, item):
        """
        Insert an item at the front of the deque.
        
        Parameters:
        item : any
            The element to be added at the front.
        """
        self.deque.appendleft(item)

    def insert_rear(self, item):
        """
        Insert an item at the rear of the deque.
        
        Parameters:
        item : any
            The element to be added at the rear.
        """
        self.deque.append(item)

    def remove_front(self):
        """
        Remove and return the item from the front of the deque.
        
        Returns:
        any
            The element removed from the front.
        
        Raises:
        IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        return self.deque.popleft()

    def remove_rear(self):
        """
        Remove and return the item from the rear of the deque.
        
        Returns:
        any
            The element removed from the rear.
        
        Raises:
        IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        return self.deque.pop()

    def display(self):
        """
        Display the contents of the deque.
        
        Returns:
        str
            A string representation of the deque.
        """
        return str(list(self.deque))

    def is_empty(self):
        """
        Check if the deque is empty.
        
        Returns:
        bool
            True if empty, False otherwise.
        """
        return len(self.deque) == 0

    def size(self):
        """
        Return the number of items in the deque.
        
        Returns:
        int
            The size of the deque.
        """
        return len(self.deque)
    
dq = DequeDS()
dq.insert_rear(10)
dq.insert_front(20)
dq.insert_rear(30)

print(dq.display())       # Output: [20, 10, 30]
print(dq.remove_front())  # Output: 20
print(dq.remove_rear())   # Output: 30
print(dq.size())          # Output: 1
print(dq.is_empty())      # Output: False




"""Task Description #9 Real-Time Application Challenge – Choose the
Right Data Structure
Scenario:
Your college wants to develop a Campus Resource Management System
that handles:
1. Student Attendance Tracking – Daily log of students
entering/exiting the campus.
2. Event Registration System – Manage participants in events with
quick search and removal.
3. Library Book Borrowing – Keep track of available books and their
due dates.
4. Bus Scheduling System – Maintain bus routes and stop
connections.
5. Cafeteria Order Queue – Serve students in the order they arrive.
Student Task:
• For each feature, select the most appropriate data structure from
the list below:
o Stack
o Queue
o Priority Queue
o Linked List
o Binary Search Tree (BST)
o Graph
o Hash Table
o Deque
• Justify your choice in 2–3 sentences per feature.
• Implement one selected feature as a working Python program with
AI-assisted code generation.
Expected Output:
• A table mapping feature → chosen data structure → justification.
• A functional Python program implementing the chosen feature
with comments and docstrings."""


import heapq
from datetime import datetime

class LibrarySystem:
    """
    Library Book Borrowing System using a Priority Queue.
    Books are prioritized by their due date (earliest due date = highest priority).
    """

    def __init__(self):
        self.borrowed_books = []  # Min-heap based on due date

    def borrow_book(self, title, due_date):
        """
        Borrow a book and add it to the priority queue.
        
        Parameters:
        title : str
            The title of the book.
        due_date : str (YYYY-MM-DD)
            The due date for returning the book.
        """
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        heapq.heappush(self.borrowed_books, (due_date_obj, title))

    def next_due_book(self):
        """
        Get the book with the nearest due date.
        
        Returns:
        str
            Title of the book due soonest.
        """
        if not self.borrowed_books:
            return "No borrowed books."
        return self.borrowed_books[0][1]

    def return_book(self):
        """
        Return the book with the nearest due date.
        
        Returns:
        str
            Title of the returned book.
        """
        if not self.borrowed_books:
            return "No borrowed books."
        return heapq.heappop(self.borrowed_books)[1]

    def display_books(self):
        """
        Display all borrowed books sorted by due date.
        
        Returns:
        str
            A string representation of borrowed books.
        """
        return [f"{title} (Due: {due.strftime('%Y-%m-%d')})" for due, title in sorted(self.borrowed_books)]
    
library = LibrarySystem()
library.borrow_book("Data Structures", "2026-03-20")
library.borrow_book("AI Research", "2026-03-18")
library.borrow_book("Python Basics", "2026-03-25")

print("Next due book:", library.next_due_book())  
# Output: AI Research

print("Returning:", library.return_book())  
# Output: AI Research

print("Borrowed Books:", library.display_books())  
# Output: ['Data Structures (Due: 2026-03-20)', 'Python Basics (Due: 2026-03-25)']







"""Task Description #10: Smart E-Commerce Platform – Data Structure
Challenge
An e-commerce company wants to build a Smart Online Shopping System
with:
1. Shopping Cart Management – Add and remove products
dynamically.
2. Order Processing System – Orders processed in the order they are
placed.
3. Top-Selling Products Tracker – Products ranked by sales count.
4. Product Search Engine – Fast lookup of products using product ID.
5. Delivery Route Planning – Connect warehouses and delivery
locations.
Student Task:
• For each feature, select the most appropriate data structure from
the list below:
o Stack
o Queue
o Priority Queue
o Linked List
o Binary Search Tree (BST)
o Graph
o Hash Table
o Deque
• Justify your choice in 2–3 sentences per feature.
• Implement one selected feature as a working Python program with
AI-assisted code generation.
Expected Output:
• A table mapping feature → chosen data structure → justification.
• A functional Python program implementing the chosen feature
with comments and docstrings."""


class OrderQueue:
    """
    Order Processing System using a Queue (FIFO).
    Ensures orders are processed in the order they are placed.
    """

    def __init__(self):
        self.queue = []

    def place_order(self, order_id):
        """
        Add a new order to the queue.
        
        Parameters:
        order_id : str
            Unique identifier for the order.
        """
        self.queue.append(order_id)

    def process_order(self):
        """
        Process the next order in the queue.
        
        Returns:
        str
            The order ID being processed.
        
        Raises:
        IndexError: If no orders are in the queue.
        """
        if self.is_empty():
            raise IndexError("No orders to process")
        return self.queue.pop(0)

    def peek_next_order(self):
        """
        View the next order without processing it.
        
        Returns:
        str
            The next order ID.
        
        Raises:
        IndexError: If no orders are in the queue.
        """
        if self.is_empty():
            raise IndexError("No orders in queue")
        return self.queue[0]

    def is_empty(self):
        """
        Check if the order queue is empty.
        
        Returns:
        bool
            True if empty, False otherwise.
        """
        return len(self.queue) == 0

    def display_orders(self):
        """
        Display all pending orders.
        
        Returns:
        list
            List of order IDs in the queue.
        """
        return self.queue

orders = OrderQueue()
orders.place_order("ORD001")
orders.place_order("ORD002")
orders.place_order("ORD003")

print("Next order:", orders.peek_next_order())   # Output: ORD001
print("Processing:", orders.process_order())     # Output: ORD001
print("Pending Orders:", orders.display_orders()) # Output: ['ORD002', 'ORD003']