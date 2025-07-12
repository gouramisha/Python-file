def is_palindrome_recursive(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome_recursive(s, start + 1, end - 1)

# Example
s = "racecar"
if is_palindrome_recursive(s, 0, len(s) - 1):
    print("Palindrome")
else:
    print("Not Palindrome")
