n = 3

for i in range(1, n+1):
    for j in range(1, n+1):
        # Border stars
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to next line


# Multiplication Table of n in Reverse Order
n = int(input("Enter a number: "))

for i in range(10, 0, -1):  # Start from 10 to 1, step -1
    print(f"{n} x {i} = {n * i}")