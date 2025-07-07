from re import S


sum = lambda a, y : a+y
print(sum(5,3))

# square
square = lambda x :x*x
print(square(3))

#string
to_uppercase = lambda s: s.upper()
print(to_uppercase("hello"))    # Output: HELLO

# Ek lambda banao jo name ko uppercase kare

# Ek lambda banao jo 3 numbers me se maximum bataye

# Ek lambda banao jo check kare number positive hai ya negative

upper = lambda s : s.upper()
print(upper("amisha"))


maximum = lambda x , y, z : max(x, y, z)
print (maximum(5, 9, 8))


check_sign = lambda n: "Positive" if n > 0 else "Negative"
print(check_sign(56))   # Output: Positive
print(check_sign(-10))  # Output: Negative

