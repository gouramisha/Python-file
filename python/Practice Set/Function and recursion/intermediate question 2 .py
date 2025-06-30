def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# Test
print(power(2, 3))  # Output: 8


# 3. List comprehension for multiplication table

num = int(input("Enter a number for its multiplication table: "))
table = [num * i for i in range(1, 11)]
print("Multiplication Table:", table)