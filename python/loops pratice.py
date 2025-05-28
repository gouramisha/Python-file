# Program to print the multiplication table of a number using for loop
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    
# Program to greet names starting with S
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print("Hello", name)
c