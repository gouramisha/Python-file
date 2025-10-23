def missingNumber(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)

# Example
nums = [3, 0, 1]
print(missingNumber(nums))  # Output: 2
