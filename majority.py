def majority_element(arr):
    n = len(arr)
    for i in arr:
        if arr.count(i) > n // 2:
            return i
    return -1

arr = [2, 2, 1, 1, 2, 2, 2]
print(majority_element(arr))
