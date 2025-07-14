def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        if not swapped:
            break  # Stop early if no swaps occurred

arr = [5, 1, 4, 2, 8]
bubble_sort(arr)
print("Sorted array:", arr)
