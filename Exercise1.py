#operator
import abc
from tokenize import Exponent


print(56)
print(5+6)
print(15-6)
print(15*6)
print(15/6)
print(5//6)
print(5%3)
#Exponent
print(5**5)

#Exercise 1 - create a Calculator
a = 50
b = 3
print("The value of ", a, " + ", 3, "is: ", a + b)
print("The value of ", a, " - ", 3, "is: ", a - b)
print("The value of ", a, " * ", 3, "is: ", a * b)
print("The value of ", a, " / ", 3, "is: ", a / b)
print("The value of ", a, " // ", 3, "is: ", a // b)
# shoutcut key Alt +  shift + Down Replicate value
a = input("Enter the first number: ")
b = input("Enter the operator (+, -, *, /): ")
c = input("Enter the second number: ")

print("The Answer is =", eval(a + b + c))
 
