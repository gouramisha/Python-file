# Reverse Number

num = 12345  # Example number
print("Digits in the number are:")

while num > 0:
    digit = num % 10         # Get the last digit
    print(digit)             # Print the digit
    num = num // 10          # Remove the last digit


# this is changes for temp