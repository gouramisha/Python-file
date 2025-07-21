def is_sorted(arr):
    n = len(arr)

    # Traverse through the array
    for i in range(n - 1):
        # If the current element is greater than the next one
        if arr[i] > arr[i + 1]:
            return False  # Not sorted

    return True  # Sorted

# ✅ Test Cases
arr1 = [1, 2, 3, 4, 5]
arr2 = [10, 5, 7, 8]
arr3 = [3, 3, 5, 7]  # Duplicate elements also allowed in sorted

print("Is arr1 sorted?:", is_sorted(arr1))  # True
print("Is arr2 sorted?:", is_sorted(arr2))  # False
print("Is arr3 sorted?:", is_sorted(arr3))  # True
