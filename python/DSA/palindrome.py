# n = 1234
# num = n
# result = 0
# while num > 0:
#     ld = num % 10
#     result = (result * 10) + ld
#     num = num // 10

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10            # Last digit nikaalna
    reverse = reverse * 10 + digit  # Reverse banana
    num = num // 10             # Last digit hataana

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")

