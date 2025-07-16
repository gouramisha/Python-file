# Array: [7, 2, 1, 6, 8, 5, 3, 4]

# Step 1: Pivot = 4
# Divide: 
#    Left:  [2, 1, 3]   (chhote)
#    Pivot: [4]
#    Right: [7, 6, 8, 5]  (bade)

# Step 2: Recursively sort left and right
# [1, 2, 3] + [4] + [5, 6, 7, 8]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

# Try it!
arr = [7, 2, 1, 6, 8, 5, 3, 4]
print("Sorted:", quick_sort(arr))
