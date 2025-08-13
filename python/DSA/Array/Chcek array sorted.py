#  Check if Array is Sorted

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2]))    # Output: False