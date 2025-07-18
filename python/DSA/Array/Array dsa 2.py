def find_second_largest(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second

print(find_second_largest([12, 35, 1, 10, 34, 1]))


def find_second_largest(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second

print(find_second_largest([12, 35, 1, 10, 34, 1]))  # Output: 34

