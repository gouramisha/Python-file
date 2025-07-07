#  Sum of First n Natural Numbers Using While Loop
n = int(input("Enter n:"))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("sum of first", n, "natural numbers is:", sum)

#Star Pattern: *, ***, ***** for n = 3
n = 3
for i in range(n):
    stars = '*' * (2*i + 1)
    print(stars)
