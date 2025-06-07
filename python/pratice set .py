#Write a program to check if the number is divisible by 5 or not.
from math import factorial


num = int(input("Enter the Number"))
if num % 5 == 0:
    print("Divisible by 5")
else: 
    print("Not Divisible by 5")



#Write a program to calculate area of rectangle (length × breadth).
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
print("The area of rectangle is:", area)


#Write a program that takes your birth year and shows your age.
birth_year = int(input("Your date of Birth Year? "))
age = 2025 - birth_year
print("Your Age:", age)

#Calculate a factorial 
num = int(input("Enter a number"))
factorial = 1
for i in range (1, num+1):
 factorial = factorial * i
print("The fractorial of", num , "is", factorial)

# Reverse a String
string = input("Enter a string")
reverse_string = string[:: -2]
print("Revesed String", reverse_string)




