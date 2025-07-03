# ✅ 1. Constant Time — O(1)

def get_first_item(lst):
    return lst[0]

get_first_item([10, 20, 30])
# 📌 Why? Only 1 operation — getting the first element.

# ✅ 2. Linear Time — O(n)

def print_all_items(lst):
    for item in lst:
        print(item)

print_all_items([10, 20, 30])
# 📌 Why? Goes through each element one by one.

# ✅ 3. Quadratic Time — O(n²)

def print_pairs(lst):
    for i in lst:
        for j in lst:
            print(i, j)

print_pairs([1, 2, 3])
# 📌 Why? Nested loops → for every i, inner loop runs again.

# ✅ 4. Logarithmic Time — O(log n)

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

binary_search([1, 3, 5, 7, 9], 7)
# 📌 Why? Each time, it cuts the list in half.

# ✅ 5. Appending to a List — O(1) (Amortized)

lst = []
for i in range(10):
    lst.append(i)
# 📌 Why? Adding at the end of the list is fast.


def contains(lst, x):
    return x in lst

contains([1, 2, 3, 4], 3)
# 📌 Why? It checks each item until it finds the match.

# Do you want me to make a quiz, or explain how to analyze your own code's time complexity?

