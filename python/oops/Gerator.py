# ✅ What is a Generator?
# A generator is a function that returns an iterator, but instead of returning all the values at once, it yields one value at a time using the yield keyword.
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

for value in gen:
    print(value)
# 💡 Generator kya hota hai?
# Ek function hota hai jo yield keyword ka use karta hai.

# Ye ek-ek karke value deta hai (memory efficient).

# Har bar yield se function pause ho jata hai, resume hota hai next time.
# 🔁 return vs yield
# return	yield
# Function ko end karta hai	Function ko pause karta hai
# Ek hi value deta hai	Ek-ek karke values deta hai

