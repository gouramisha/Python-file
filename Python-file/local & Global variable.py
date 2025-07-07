# Global Vaeriable
x = 10 
def my_function():
     print("Function ke andar x =", x)  # Global variable dikh raha hai

my_function()

print("Function ke bahar x =", x)  # Global variable yahan bhi dikh raha hai
 


# Local variable
def my_function():
    y = 5  # Local variable
    print("Function ke andar y =", y)

my_function()

print("Function ke bahar y =", y)  # Error! Kyunki y sirf function ke andar tha




