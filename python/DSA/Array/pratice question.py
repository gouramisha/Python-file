# . Find the Largest Element

def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

arr = [3, 7, 2, 9, 5]
print(find_largest(arr))  