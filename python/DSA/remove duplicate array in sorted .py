def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0  # Yeh mummy ka tray hai
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:  # Nayi chocolate aayi?
            i += 1
            arr[i] = arr[j]  # Rakh lo!

    return i + 1  # Total chocolates mummy ne rakhne diya

# Try karo
arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
naya_length = remove_duplicates(arr)
print("Chocolates (unique):", arr[:naya_length])
