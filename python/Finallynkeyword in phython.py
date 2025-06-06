# 🔹 Real Example: User se number input

try:
    num = int(input("Koi number dijiye: "))
    print("Aapka number:", num)
except ValueError:
    print("Please sirf number dijiye, letters nahi.")
# else aur finally ke saath:

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", num)
finally:
    print("Yeh hamesha chalega.")
# else: Jab koi error na aaye.

# finally: Hamesha chalega, chahe error aaye ya na aaye.

# 🔥 Common Exceptions:
# Exception	Kab aata hai
# ZeroDivisionError	Jab zero se divide karte ho
# ValueError	Jab galat type ka input dete ho
# IndexError	Jab list ke bahar index access karte ho
# KeyError	Dictionary mein galat key access karte ho

# 🔚 Summary:
# try block mein risky code likha jata hai.

# except block mein error handle hoti hai.

# try se aapka program crash nahi hota, balki gracefully handle hota hai.
