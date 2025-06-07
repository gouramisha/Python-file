#Fibonacci Series
num = int(input("Enter the number"))
a = 0
b = 1
print ("Fabonacci series")
for i in range (num):
    print(a, end=" ")
    c = a + b
    a = b 
    b = c



# Find GCD
a = int(input("Enter 1 number"))
b = int(input("Enter 2 nd number"))
while b != 0:
 a, b = b, a % b

print("GCD is:", a)



