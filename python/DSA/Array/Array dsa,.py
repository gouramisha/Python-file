# nums = [11, 20 , 330 , -9 ]
# largest = nums[0]
# n = len (nums)
# for i in range (0, n):
#     largest max(largest , nums[i])

arr = [4, 9, 1, 17, 3]

# Step 1: Assume first number is biggest
largest = arr[0]

# Step 2: Check every number
for num in arr:
    if num > largest:
        largest = num

# Step 3: Print result
print("Largest number is:", largest)
 
   