# Q1: Write a function to count vowels in a string.
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Test
print(count_vowels("Hello World"))  # Output: 3
