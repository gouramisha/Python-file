def merge_sorted_arrays(arr1, arr2):
    i = j = 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not merged or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not merged or merged[-1] != arr2[j]:
                merged.append(arr2[j])
            j += 1
        else:  # arr1[i] == arr2[j]
            if not merged or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements from arr1
    while i < len(arr1):
        if not merged or merged[-1] != arr1[i]:
            merged.append(arr1[i])
        i += 1

    # Add remaining elements from arr2
    while j < len(arr2):
        if not merged or merged[-1] != arr2[j]:
            merged.append(arr2[j])
        j += 1

    return merged
