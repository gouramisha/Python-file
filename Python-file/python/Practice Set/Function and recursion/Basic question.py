#  Add Two Numbers Using a Function
from numpy import negative


def add(a, b):
    return a + b

print("Sum:", add(3, 4))  # Output: 7

#Write a function to return the square of a number.

def square(n):
    return n * n

print(square(4))  

#Write a function to find the maximum of three numbers.
def max_of_three(a, b, c):
    return max(a, b,c)
print (max_of_three (10, 20 , 30))

#Write a function to check whether a number is positive, negative or zero.
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-5))  # Output: Negative

# Write a function to calculate the factorial of a number using recursion.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Write a function to calculate the factorial of a number using recursion.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Write a recursive function to calculate the sum of first n natural numbers.

def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)

print(sum_n(5))  # Output: 15

#Star Pattern *, ***, ***** for n = 3 (with Function)

def star_pattern_odd(n):
    for i in range(n):
        print("*" * (2*i + 1))

star_pattern_odd(3)


