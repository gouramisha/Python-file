#1.Write a program to print Twinkle twinkle little star poem in python.
print("Twinkle, Twinkle, Little Star \n How I wonder what you are!\n up above the world so high \n like a diamond in the sky\n")

#2..print the table of 5 using it
number = 5  # Hamne bola ki humein 5 ka table chahiye

for i in range(1, 11):  # Yeh loop 1 se 10 tak chalega (1, 2, ..., 10)
    print(number,'x',i,'=', number*i)   # Yeh line table ka ek ek step print karegi
    #f-string ka kaam:
# Jahaan {} likha hota hai, Python uske andar jo bhi cheez hai usko calculate karke us jagah daal deta hai.

# 3. giva a input then print a table 
num =int(input("Enter any number"))
for i in range (1, 11):
    print(num,'x',i,'=', num*i) 


#4.import os  # Python ka helper bula liya

# Apna almari ka path bataya
path = " "  # Yahan apna folder ka rasta likho

# Dekhte hain is almari mein kya kya hai
items = os.listdir(path)

# Ab sab cheezen ek ek karke print karo
for item in items:
    print(item)