def reverse_array(arr, start, end):
    if start >= end:
        return
    # Swap elements
    arr[start], arr[end] = arr[end], arr[start]
    # Recursive call
    reverse_array(arr, start + 1, end - 1)

# Example usage
arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, len(arr) - 1)
print("Reversed array:", arr)