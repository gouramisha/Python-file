# CHAPTER 5 – DICTIONARY & SETS   
# Dictionary is a collection of keys-value pairs.
# a = {
# "key": "value",
# "harry": "code",
# "marks": "100",
# "list": [1, 2, 9]
# }
# print(a["key"])   # Output: "value"
# print(a["list"])  # Output: [1, 2, 9]

# # Dict 
# car = {
#     "brand": "Toyota",
#     "model": "Camry",
#     "year": 2020
# }

# print(car["model"])   # Output kya hoga

# Sets
# Set is a collection of non-repetitive elements.
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.
# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
# Hindi to English dictionary
# c


# Write a program to input eight numbers from the user and display all the unique numbers (once).
# Program to input 8 numbers and display unique numbers

# Step 1: Input 8 numbers
# numbers = []
# for i in range(8):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# # Step 2: Find and display unique numbers
# unique_numbers = list(set(numbers))

# print("\nUnique numbers are:")
# for num in unique_numbers:
#     print(num)

#Can we have a set with 18 (int) and '18' (str) as a value in it?
# my_set = {18, "18"}
# print(my_set)

# #What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?



print(len(s))

s = {}
print(type(s))

#Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique
my_dict = {}


for i in range(4):
    name = input(f"Enter Yor name {i+1}")
    lngauge =  input(f"Hey {name} Enter your fav langaue") 
    my_dict[name] = lngauge

print (my_dict)

# my_dict['Alice'] = input("Hey Alic enter your fav lan: ")
# my_dict['Bob'] = input("Hey bob enter your fav lan: ")
# my_dict['Charlie'] = input("Hey Charlie enter your fav lan: ")
# my_dict['Diana'] = input("Hey Diana enter your fav lan: ")

# print(my_dict)

#If the names of 2 friends are same; what will happen to the program in problem 6


# ANS ==> 