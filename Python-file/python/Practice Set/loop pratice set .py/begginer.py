
# 🔁 Basic Loop Questions with Code
# 1. Print numbers from 1 to 10 using for loop
# for i in range(1, 11):
#     print(i)
# # 2. Print all even numbers from 1 to 50 using while loop

# i = 1
# while i <= 50:
#     if i % 1 == 0:
#         print(i)
#     i += 1
# # 3. Print multiplication table of a given number

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")
# # 4. Print star pattern

# # *
# # **
# # ***
# # ****
# # *****
# for i in range(1, 6):
#     print("*" * i)
# # 5. Sum of first n natural numbers

n = int(input("Enter n: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum is:", sum)