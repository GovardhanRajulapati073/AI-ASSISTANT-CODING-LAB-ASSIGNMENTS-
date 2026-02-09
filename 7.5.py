#Task 1 (Mutable Default Argument – Function Bug)
#Task: Analyze given code where a mutable default argument causes unexpected behavior. Use AI to fix it.
# Bug: Mutable default argument
"""def add_item(item, items=[]):
    items.append(item)
    return items
print(add_item(1))
print(add_item(2))"""
#Expected Output: Corrected function avoids shared list bug.
#Fixed code
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item(1))  # [1]
print(add_item(2))  # [2]




#Task 2 (Floating-Point Precision Error)
#Task: Analyze given code where floating-point comparison fails.     Use AI to correct with tolerance.
# Bug: Floating point precision issue
"""def check_sum():
    return (0.1 + 0.2) == 0.3
print(check_sum())"""
#Expected Output: Corrected function 

#Fixed code
def check_sum():
    return abs((0.1 + 0.2) - 0.3) < 1e-9
print(check_sum())





#Task 3 (Recursion Error – Missing Base Case)
#Task: Analyze given code where recursion runs infinitely due to missing base case. Use AI to fix.
# Bug: No base case
"""def countdown(n):
    print(n)
    return countdown(n-1)
countdown(5)"""
#Expected Output : Correct recursion with stopping condition.	
#Fixed code
def countdown(n):
    if n <= 0:   # base case
        print("Done!")
        return
    print(n)
    return countdown(n-1)
countdown(5)






#Task 4 (Dictionary Key Error)
#Task: Analyze given code where a missing dictionary key causes error. Use AI to fix it.
# Bug: Accessing non-existing key
"""def get_value():
    data = {"a": 1, "b": 2}
    return data["c"]
print(get_value())"""
#Expected Output: Corrected with .get() or error handling.
#Fixed code
def get_value():
    data = {"a": 1, "b": 2}
    return data.get("c", "Key not found")
print(get_value())





#Task 5 (Infinite Loop – Wrong Condition)
#Task: Analyze given code where loop never ends. Use AI to detect and fix it.
# Bug: Infinite loop
"""def loop_example():
    i = 0
    while i < 5:
        print(i)"""
#Expected Output: Corrected loop increments i.
#Fixed code
def loop_example():
    i = 0
    while i < 5:
        print(i)
        i += 1  # Increment to avoid infinite loop
loop_example()





#Task 6 (Unpacking Error – Wrong Variables)
#Task: Analyze given code where tuple unpacking fails. Use AI to fix it.
# Bug: Wrong unpacking
"""a, b = (1, 2, 3)"""
#Expected Output: Correct unpacking or using _ for extra values.
#Fixed code
a, b, _ = (1, 2, 3)  # Using _ to ignore the extra value
print(a, b)




#Task 7 (Mixed Indentation – Tabs vs Spaces)
#Task: Analyze given code where mixed indentation breaks execution. Use AI to fix it.
# Bug: Mixed indentation
"""def func():
    x = 5
        y = 10
    return x+y"""
#Expected Output : Consistent indentation applied.
#Fixed code
def func():
    x = 5
    y = 10
    return x + y
print(func())




#Task 8 (Import Error – Wrong Module Usage)
#Task: Analyze given code with incorrect import. Use AI to fix.
# Bug: Wrong import
"""import maths
print(maths.sqrt(16))"""
#Expected Output: Corrected to import math
#Fixed code
import math
print(math.sqrt(16))






#Task 9 (Unreachable Code – Return Inside Loop)
#Task: Analyze given code where a return inside a loop prevents full iteration. Use AI to fix it.
# Bug: Early return inside loop
"""def total(numbers):
    for n in numbers:
        return n
print(total([1,2,3]))"""
#Expected Output: Corrected code accumulates sum and returns after loop

def total(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum
print(total([1, 2, 3]))  # Output: 6





#Task 10 (Name Error – Undefined Variable)
#Task: Analyze given code where a variable is used before being defined. Let AI detect and fix the error.
# Bug: Using undefined variable
"""def calculate_area():
return length * width
print(calculate_area())"""
#Requirements:•	Run the code to observe the error. •	Ask AI to identify the missing variable definition. •	Fix the bug by defining length and width as parameters.•	Add 3 assert test cases for correctness.
#Expected Output :•	Corrected code with parameters.•	AI explanation of the bug. Successful execution of assertions.

def calculate_area(length, width):
    return length * width
#AI Explanation: The original code attempts to use the variables 'length' and 'width' without defining them, which results in a NameError.
#By defining 'length' and 'width' as parameters of the function, we can pass the necessary values when calling the function, thus fixing the error.
#Test cases 
assert calculate_area(5, 10) == 50
assert calculate_area(3, 4) == 12
assert calculate_area(7, 2) == 14
print(calculate_area(5, 10))  # Output: 50




#Task 11 (Type Error – Mixing Data Types Incorrectly)
#Task: Analyze given code where integers and strings are added incorrectly. Let AI detect and fix the error.
# Bug: Adding integer and string
"""def add_values():
    return 5 + "10"
print(add_values())"""
#Requirements: •	Run the code to observe the error. •	AI should explain why int + str is invalid. •	Fix the code by type conversion (e.g., int("10") or str(5)). •	Verify with 3 assert cases.
#Expected Output #6: •	Corrected code with type handling.•	AI explanation of the fix. Successful test validation.
def add_values():
    return 5 + int("10")
#AI Explanation: The original code attempts to add an integer (5) and a string ("10"), which is not allowed in Python and results in a TypeError.
#By converting the string "10" to an integer using int("10"), we can perform the addition correctly without any errors.
#Test cases 
assert add_values() == 15
print(add_values())  # Output: 15






#Task 12 (Type Error – String + List Concatenation)
#Task: Analyze code where a string is incorrectly added to a list.
# Bug: Adding string and list
"""def combine():
    return "Numbers: " + [1, 2, 3]
print(combine())"""
#Requirements: •	Run the code to observe the error. •	Explain why str + list is invalid. •	Fix using conversion (str([1,2,3]) or " ".join()). •	Verify with 3 assert cases.
# Output: •	Corrected code •	Explanation •	Successful test validation
def combine():
    return "Numbers: " + str([1, 2, 3])
#AI Explanation: The original code attempts to concatenate a string ("Numbers: ") with a list ([1, 2, 3]), which is not allowed in Python and results in a TypeError.
#By converting the list to a string using str([1, 2, 3]), #we can concatenate it with the string without any errors.
#Test cases
assert combine() == "Numbers: [1, 2, 3]"
print(combine())  # Output: Numbers: [1, 2, 3]






#Task 13 (Type Error – Multiplying String by Float)
#Task: Detect and fix code where a string is multiplied by a float.
# Bug: Multiplying string by float
"""def repeat_text():
    return "Hello" * 2.5
print(repeat_text())"""
#Requirements: •	Observe the error. •	Explain why float multiplication is invalid for strings. •	Fix by converting float to int. •	Add 3 assert test cases.
#Expected Output: •	Corrected code with type handling.•	AI explanation of the fix. Successful test validation.
def repeat_text():
    return "Hello" * int(2.5)
#AI Explanation: The original code attempts to multiply a string ("Hello") by a float (2.5), which is not allowed in Python and results in a TypeError.
#By converting the float to an integer using int(2.5), we can repeat the string a whole number of times without any errors.
#Test cases
assert repeat_text() == "HelloHello"
print(repeat_text())  # Output: HelloHello





#Task 14 (Type Error – Adding None to Integer)
#Task: Analyze code where None is added to an integer.
# Bug: Adding None and integer
"""def compute():
    value = None
    return value + 10
print(compute())"""
#Requirements: •Run and identify the error. •	Explain why NoneType cannot be added. •	Fix by assigning a default value. •	Validate using asserts.
#Expected Output: •	Corrected code with default value.•	AI explanation of the fix. Successful test validation.
def compute():
    value = None
    if value is None:
        value = 0  # Assign a default value
    return value + 10
#AI Explanation: The original code attempts to add None (which is of type NoneType) to an integer (10), which is not allowed in Python and results in a TypeError.
#By checking if value is None and assigning it a default value (0 in this case), we can perform the addition without any errors.
#Test cases
assert compute() == 10
print(compute())  # Output: 10





#Task 15 (Type Error – Input Treated as String Instead of Number)
#Task: Fix code where user input is not converted properly.
# Bug: Input remains string
"""def sum_two_numbers():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    return a + b
print(sum_two_numbers())"""
#Requirements:•	Explain why input is always string.•	Fix using int() conversion.•	Verify with assert test cases.
#Expected Output: •	Corrected code with input conversion.•	AI explanation of the fix. Successful test validation.
def sum_two_numbers():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    return int(a) + int(b)
#AI Explanation: The input() function in Python always returns a string, even if the user enters a number.
#By converting the input strings to integers using int(), we can perform numerical addition instead of string concatenation, thus fixing the error.
#Test cases
# Note: Since input() requires user interaction, we will not run assert test cases here. Instead, you can test the function by running it and entering numbers when prompted.
print(sum_two_numbers())  # Example input: 5 and 10, Output: 15

