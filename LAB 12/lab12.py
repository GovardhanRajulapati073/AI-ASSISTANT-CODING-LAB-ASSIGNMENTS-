#Lab 12: Algorithms with AI Assistance Sorting, Searching, and Algorithm Optimization Using AI Tools

"""Task 1: Sorting Student Records for Placement Drive
Scenario
SR University’s Training and Placement Cell needs to shortlist candidates
efficiently during campus placements. Student records must be sorted by
CGPA in descending order.
Tasks
1. Use GitHub Copilot to generate a program that stores student records
(Name, Roll Number, CGPA).
2. Implement the following sorting algorithms using AI assistance:
o Quick Sort
o Merge Sort
3. Measure and compare runtime performance for large datasets.
4. Write a function to display the top 10 students based on CGPA.
Expected Outcome
• Correctly sorted student records.
• Performance comparison between Quick Sort and Merge Sort.
• Clear output of top-performing students."""


"""import random
import time

class Student:
    def __init__(self, name, roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa

    def __repr__(self):
        return f"{self.name} ({self.roll}) - CGPA: {self.cgpa}"

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2].cgpa
    left = [x for x in arr if x.cgpa > pivot]
    middle = [x for x in arr if x.cgpa == pivot]
    right = [x for x in arr if x.cgpa < pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].cgpa >= right[j].cgpa:  # descending order
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Generate large dataset
students = [Student(f"Student{i}", i, round(random.uniform(5.0, 10.0), 2)) for i in range(10000)]

# Quick Sort timing
start = time.time()
qs_sorted = quick_sort(students)
qs_time = time.time() - start

# Merge Sort timing
start = time.time()
ms_sorted = merge_sort(students)
ms_time = time.time() - start

print(f"Quick Sort Time: {qs_time:.5f} seconds")
print(f"Merge Sort Time: {ms_time:.5f} seconds")
"""




"""Task 2: Implementing Bubble Sort with AI Comments
• Task: Write a Python implementation of Bubble Sort.
• Instructions:
• Students implement Bubble Sort normally.
• Ask AI to generate inline comments explaining key logic (like
swapping, passes, and termination).
• Request AI to provide time complexity analysis.
• Expected Output:
• A Bubble Sort implementation with AI-generated explanatory
comments and complexity analysis."""


"""def bubble_sort(arr):
    n = len(arr)
    # Outer loop for each pass through the array
    for i in range(n):
        # Flag to check if any swapping happened in this pass
        swapped = False
        
        # Inner loop compares adjacent elements
        for j in range(0, n - i - 1):
            # If the current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swapping
                swapped = True
        
        # If no swaps occurred, array is already sorted → terminate early
        if not swapped:
            break
    return arr


# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
print("Original:", data)
sorted_data = bubble_sort(data)
print("Sorted:", sorted_data)"""





"""Task 3: Quick Sort and Merge Sort Comparison
• Task: Implement Quick Sort and Merge Sort using recursion.
• Instructions:
• Provide AI with partially completed functions for recursion.
• Ask AI to complete the missing logic and add docstrings.
• Compare both algorithms on random, sorted, and reverse-sorted
lists.
• Expected Output:
• Working Quick Sort and Merge Sort implementations.
• AI-generated explanation of average, best, and worst-case
complexities."""


"""def quick_sort(arr):
    
    Recursive Quick Sort implementation.
    
    Args:
        arr (list): List of numbers to sort.
    
    Returns:
        list: Sorted list in ascending order.
    
    Logic:
    - Choose a pivot (middle element).
    - Partition into left (< pivot), middle (= pivot), right (> pivot).
    - Recursively sort left and right partitions.
    
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    
    Recursive Merge Sort implementation.
    
    Args:
        arr (list): List of numbers to sort.
    
    Returns:
        list: Sorted list in ascending order.
    
    Logic:
    - Divide list into two halves.
    - Recursively sort each half.
    - Merge two sorted halves into one sorted list.
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    Helper function to merge two sorted lists.
    result = []
    i = j = 0
    
    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


import random
import time

def test_algorithms():
    sizes = [1000, 5000, 10000]
    for n in sizes:
        print(f"\nDataset size: {n}")
        
        # Random list
        rand_list = [random.randint(1, 10000) for _ in range(n)]
        
        # Sorted list
        sorted_list = list(range(n))
        
        # Reverse sorted list
        reverse_list = list(range(n, 0, -1))
        
        for dataset, name in [(rand_list, "Random"), (sorted_list, "Sorted"), (reverse_list, "Reverse Sorted")]:
            # Quick Sort timing
            start = time.time()
            quick_sort(dataset)
            qs_time = time.time() - start
            
            # Merge Sort timing
            start = time.time()
            merge_sort(dataset)
            ms_time = time.time() - start
            
            print(f"{name} → Quick Sort: {qs_time:.5f}s | Merge Sort: {ms_time:.5f}s")

test_algorithms()"""





"""Task 4 (Real-Time Application – Inventory Management System)
Scenario: A retail store’s inventory system contains thousands of products,
each with attributes like product ID, name, price, and stock quantity. Store staff
need to:
1. Quickly search for a product by ID or name.
2. Sort products by price or quantity for stock analysis.
Task:
• Use AI to suggest the most efficient search and sort algorithms for this
use case.
• Implement the recommended algorithms in Python.
• Justify the choice based on dataset size, update frequency, and
performance requirements.
Expected Output:
• A table mapping operation → recommended algorithm → justification.
• Working Python functions for searching and sorting the inventory."""



"""class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.product_id} | {self.name} | Price: {self.price} | Qty: {self.quantity}"
    

# Search by Product ID using dictionary
def build_inventory_dict(products):
    return {p.product_id: p for p in products}

def search_by_id(inventory_dict, product_id):
    return inventory_dict.get(product_id, "Product not found")

# Search by Product Name using Binary Search
def binary_search_by_name(sorted_products, target_name):
    low, high = 0, len(sorted_products) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_products[mid].name == target_name:
            return sorted_products[mid]
        elif sorted_products[mid].name < target_name:
            low = mid + 1
        else:
            high = mid - 1
    return "Product not found"


# Merge Sort by Price
def merge_sort_price(products):
    if len(products) <= 1:
        return products
    mid = len(products) // 2
    left = merge_sort_price(products[:mid])
    right = merge_sort_price(products[mid:])
    return merge_price(left, right)

def merge_price(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].price <= right[j].price:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Quick Sort by Quantity
def quick_sort_quantity(products):
    if len(products) <= 1:
        return products
    pivot = products[len(products) // 2].quantity
    left = [p for p in products if p.quantity < pivot]
    middle = [p for p in products if p.quantity == pivot]
    right = [p for p in products if p.quantity > pivot]
    return quick_sort_quantity(left) + middle + quick_sort_quantity(right)

# Sample inventory
products = [
    Product(101, "Laptop", 55000, 12),
    Product(102, "Mouse", 500, 150),
    Product(103, "Keyboard", 1200, 85),
    Product(104, "Monitor", 8000, 40),
]

# Build dictionary for ID search
inventory_dict = build_inventory_dict(products)
print(search_by_id(inventory_dict, 102))  # Search by ID

# Sort by name for binary search
sorted_by_name = sorted(products, key=lambda p: p.name)
print(binary_search_by_name(sorted_by_name, "Monitor"))  # Search by name

# Sort by price
sorted_by_price = merge_sort_price(products)
print("Sorted by Price:", sorted_by_price)

# Sort by quantity
sorted_by_quantity = quick_sort_quantity(products)
print("Sorted by Quantity:", sorted_by_quantity)"""






"""Task 5: Real-Time Stock Data Sorting & Searching
Scenario:
An AI-powered FinTech Lab at SR University is building a tool for analyzing
stock price movements. The requirement is to quickly sort stocks by daily
gain/loss and search for specific stock symbols efficiently.
• Use GitHub Copilot to fetch or simulate stock price data (Stock
Symbol, Opening Price, Closing Price).
• Implement sorting algorithms to rank stocks by percentage change.
• Implement a search function that retrieves stock data instantly when a
stock symbol is entered.
• Optimize sorting with Heap Sort and searching with Hash Maps.
• Compare performance with standard library functions (sorted(), dict
lookups) and analyze trade-offs."""


import random

class Stock:
    def __init__(self, symbol, opening, closing):
        self.symbol = symbol
        self.opening = opening
        self.closing = closing
        self.change = ((closing - opening) / opening) * 100  # % change

    def __repr__(self):
        return f"{self.symbol}: Open={self.opening}, Close={self.closing}, Change={self.change:.2f}%"

# Simulate dataset
symbols = ["AAPL", "GOOG", "MSFT", "TSLA", "AMZN", "NFLX", "META", "NVDA"]
stocks = [Stock(sym, random.uniform(100, 500), random.uniform(100, 500)) for sym in symbols]

# Build dictionary for instant lookup
stock_dict = {s.symbol: s for s in stocks}

def search_stock(symbol):
    return stock_dict.get(symbol, "Stock not found")

print(search_stock("TSLA"))

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left].change > arr[largest].change:
        largest = left
    if right < n and arr[right].change > arr[largest].change:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr[::-1]  # descending order

print("\nOriginal Stock Data:")
for s in stocks:
    print(s)

# Sort by % change using Heap Sort
sorted_heap = heap_sort(stocks.copy())
print("\nSorted by % Change (Heap Sort):")
for s in sorted_heap:
    print(s)

# Compare with Python sorted()
sorted_builtin = sorted(stocks, key=lambda s: s.change, reverse=True)
print("\nSorted by % Change (Python sorted):")
for s in sorted_builtin:
    print(s)
