n = int(input("Enter a number: "))

print("Factors of", n, "are:")

i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1


# optimization code
# import math

# n = int(input("Enter a number: "))
# print("Factors of", n, "are:")

# i = 1
# while i <= math.isqrt(n):  # isqrt(n) gives integer square root (√n)
#     if n % i == 0:
#         print(i)
#         if i != n // i:  # Avoid duplicate when i == sqrt(n)
#             print(n // i)
#     i += 1
