def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]          # Element to be inserted
        j = i - 1
        # Shift elements of arr[0...i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key       # Insert key at correct location
