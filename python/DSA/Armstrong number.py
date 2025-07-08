# n = 153 
# num = n
# total = 0
# nod = len(str(n))
# while num > 0:
#     ld = num % 10
#     total = toatl + (ld ** nod)
#     num = num // 10
#     return total == n

num = int(input("Enter a number: "))
original = num

# Step 1: Count the number of digits
count = 0
temp = num
while temp > 0:
    temp = temp // 10
    count += 1

# Step 2: Calculate the sum of digits raised to power 'count'
sum_of_power = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_power += digit ** count
    temp = temp // 10

# Step 3: Check Armstrong condition
if sum_of_power == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
