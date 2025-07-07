# Enumerate se hum list ke items ko unke numbers ke saath asani se dekh sakte hain.

fruits = ["apple", "banana", "cherry"]
for number, fruit in enumerate(fruits):
    print(number, fruit)

# if we want index start with one
for number, fruit in enumerate(fruits, start=1):
    print(number, fruit)

