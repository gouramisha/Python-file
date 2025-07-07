age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("You must be at least 18 years old.")
else:
    print("Access granted.")
    # raise ka use hum tab karte hain jab hume kudh se koi error throw (uthana) ho — chahe wo built-in error ho ya custom error.