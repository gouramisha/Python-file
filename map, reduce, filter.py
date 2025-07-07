from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# Step 1: Even numbers (filter)
even = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4, 6]

# Step 2: Square them (map)
squares = list(map(lambda x: x * x, even))       # [4, 16, 36]

# Step 3: Sum them (reduce)
result = reduce(lambda x, y: x + y, squares)     # 56

print(result)  # Output: 56
