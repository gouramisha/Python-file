def rearrange_max_min(arr):
    arr.sort()
    result = []
    i, j = 0, len(arr)-1
    while i <= j:
        if i != j:
            result.append(arr[j])
            result.append(arr[i])
        else:
            result.append(arr[i])
        i += 1
        j -= 1
    return result

print(rearrange_max_min([1,2,3,4,5,6,7]))
# [7, 1, 6, 2, 5, 3, 4]