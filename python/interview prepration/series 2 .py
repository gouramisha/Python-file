#  Python-Specific Concepts
# List comprehensions

# Dictionary operations

# lambda, map, filter, reduce

# Decorators

# Generators & Iterators

# Exception handling

# Object-oriented programming (OOP): class, __init__, self

# List Comprehension

# Squares of even numbers from 0 to 9
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]
# ✅ 2. Dictionary Operations

# Create and access dictionary
person = {'name': 'Alice', 'age': 25}
print(person['name'])         # Alice
person['city'] = 'Delhi'      # Add new key
print(person.get('email'))    # None (safe access)
# Dictionary comprehension:

squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# ✅ 3. lambda, map, filter, reduce

from functools import reduce

nums = [1, 2, 3, 4, 5]

# lambda
square = lambda x: x * x
print(square(3))  # 9

# map
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16, 25]

# filter
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]

# reduce
product = reduce(lambda x, y: x * y, nums)
print(product)  # 120
# ✅ 4. Decorators

def decorator_func(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
# ✅ 5. Generators & Iterators

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for val in countdown(3):
    print(val)  # 3, 2, 1

nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2
# ✅ 6. Exception Handling

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero!", e)
finally:
    print("This block always runs.")
# ✅ 7. Object-Oriented Programming (OOP)

class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

p1 = Person("Amisha", 24)
p1.greet()






