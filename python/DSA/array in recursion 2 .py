def reverseArray(arr, start, end):
    # base case
    if start >= end:
        return

    # step 1: swap start and end
    arr[start], arr[end] = arr[end], arr[start]

    # step 2: call function for next part
    reverseArray(arr, start + 1, end - 1)

# Example
arr = [1, 2, 3, 4, 5]
reverseArray(arr, 0, len(arr) - 1)
print(arr)
