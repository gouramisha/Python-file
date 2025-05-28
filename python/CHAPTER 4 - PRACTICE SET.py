# fruits = []

# # Loop to get 7 fruits from the user
# for i in range(7):
#     fruit = input(f"Enter fruit {i + 1}: ")
#     fruits.append(fruit)

# # Show the final list of fruits
# print("You entered these fruits:")
# print(fruits)

#Program to accept marks of 6 students and display them in a sorted manner

# Empty list banate hain
marks = []

# 6 students ke marks lete hain
for i in range(6):
    mark = int(input(f"Student {i+1} ke marks likho: "))
    marks.append(mark)

# Marks ko sort karte hain
marks.sort()

# Sorted marks dikhate hain
print("Sorted marks:", marks)
# 🔐 2. Check that a tuple type cannot be changed in Python
# python
# Copy
# Edit
# Tuple banate hain
my_tuple = (1, 2, 3)

# Try to change the value
# my_tuple[0] = 10  # This will give error ❌

print("Tuples can't be changed! They are fixed once created.")
# ⚠️ Agar tum my_tuple[0] = 10 likhoge, to TypeError aayega:

# php
# Copy
# Edit
# TAypeError: 'tuple' object does not support item assignment
# ➕ 3. Program to sum a list with 4 numbers
# python
# Copy
# Edit
# 4 numbers wali list
numbers = [10, 20, 30, 40]

# sum() function se total nikaalte hain
total = sum(numbers)

print("Total sum is:", total)
# 🔢 4. Program to count the number of zeros in a tuple
# python
# Copy
# Edit
a = (7, 0, 8, 0, 0, 9)

# count() se 0 ka count nikaalte hain
zero_count = a.count(0)

print("Number of zeros in tuple:", zero_count)






