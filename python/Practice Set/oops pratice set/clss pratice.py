# Class Attribute Change Through Object

class MyClass:
    a = 5  # class attribute

# Create object
obj = MyClass()
obj.a = 0  # this creates an instance attribute, doesn't change class attribute

print(MyClass.a)  # Output: 5 (unchanged)
print(obj.a)  