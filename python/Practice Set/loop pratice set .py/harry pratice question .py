n = 3

for i in range(1, n+1):
    for j in range(1, n+1):
        # Border stars
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to next line