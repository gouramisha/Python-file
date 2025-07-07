def is_palindrome(text):
    reversed_text = text[::-1]
    return text == reversed_text

# Test the function
print(is_palindrome("madam"))     # True
print(is_palindrome("racecar"))   # True
print(is_palindrome("python"))    # False
