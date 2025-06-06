#  There is two types of programing 
# 1 . object oriented programing
# 2. procedural Programming
# 🖥️ Object-Oriented Programming in Computer Language (Python Example)
# 🔹 1. Class
# Ek blueprint ya design hoti hai jisme hum data (variables) aur behavior (methods/functions) define karte hain.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
# 🔹 2. Object
# Class ka instance hota hai — jo memory me banta hai.

# python
# Copy
# Edit
# Object bana rahe hain
student1 = Student("Rahul", 18)
student2 = Student("Asha", 19)

# Object method call
student1.introduce()
student2.introduce()
# 🔹 3. Inheritance
# Ek class doosri class ke properties aur methods ko reuse karti hai.

# python
# Copy
# Edit
class Person:
#    🖥️ Object-Oriented Programming (OOP) in Python
# OOP is a way of writing code where we structure programs using objects and classes, just like things in the real world.

# 🔹 1. Class
# A class is a blueprint or template. It defines the structure and behavior (data + functions) of an object.

# python
# Copy
# Edit def speak(self):
        print("I can speak!")

# Student class Person se inherit kar rahi hai
class Student(Person):
    def study(self):
        print("I can study!")

s1 = Student()
s1.speak()   # Parent class method
s1.study()   # Child class method
# 🔹 4. Encapsulation
# Private data ko hide karna aur usse access karne ke liye methods banana.


class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(1000)
print(account.get_balance())  # Access via method
# 🔹 5. Polymorphism
# Ek hi function naam, lekin alag-alag class me different behavior.


class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

# Polymorphism in action
for animal in (Cat(), Dog()):
    animal.sound()
# ✅ Summary (Code-style Recap):
# Concept	Python Code Keyword/Use
# Class	class
# Object	object = ClassName()
# Inheritance	class Child(Parent)
# Encapsulation	__private_variable
# Polymorphism	Same method, different output

# Agar aapko ye sab ek single example ke through combine karke samjhna ho toh main ek full example bhi likh ke de sakta hoon. Bataiye?






# You said:
# 🖥️ Object-Oriented Programming in Computer Language (Python Example) --------------------------------------------------------------------- ### 🔹 1. **Class** Ek **blueprint** ya design hoti hai jisme hum data (variables) aur behavior (methods/functions) define karte hain. python CopyEdit `class Student: def __init__(self, name, age): self.name = name self.age = age def introduce(self): print(f"My name is {self.name} and I am {self.age} years old.")` * * * ### 🔹 2. **Object** **Class ka instance** hota hai — jo memory me banta hai. python CopyEdit `# Object bana rahe hain student1 = Student("Rahul", 18) student2 = Student("Asha", 19) # Object method call student1.introduce() student2.introduce()` * * * ### 🔹 3. **Inheritance** Ek class doosri class ke properties aur methods ko **reuse** karti hai. python CopyEdit `class Person: def speak(self): print("I can speak!") # Student class Person se inherit kar rahi hai class Student(Person): def study(self): print("I can study!") s1 = Student() s1.speak() # Parent class method s1.study() # Child class method` * * * ### 🔹 4. **Encapsulation** Private data ko **hide** karna aur usse access karne ke liye **methods** banana. python CopyEdit `class BankAccount: def __init__(self): self.__balance = 0 # private variable def deposit(self, amount): self.__balance += amount def get_balance(self): return self.__balance account = BankAccount() account.deposit(1000) print(account.get_balance()) # Access via method` * * * ### 🔹 5. **Polymorphism** Ek hi function naam, lekin alag-alag class me **different behavior**. python CopyEdit `class Cat: def sound(self): print("Meow") class Dog: def sound(self): print("Bark") # Polymorphism in action for animal in (Cat(), Dog()): animal.sound()` * * * ### ✅ Summary (Code-style Recap): | Concept | Python Code Keyword/Use | | --- | --- | | Class | `class` | | Object | `object = ClassName()` | | Inheritance | `class Child(Parent)` | | Encapsulation | `__private_variable` | | Polymorphism | Same method, different output | * * * Agar aapko ye sab ek single example ke through combine karke samjhna ho toh main ek full example bhi likh ke de sakta hoon. Bataiye? window.\_\_oai\_logHTML?window.\_\_oai\_logHTML():window.\_\_oai\_SSR\_HTML=window.\_\_oai\_SSR\_HTML||Date.now();requestAnimationFrame((function(){window.\_\_oai\_logTTI?window.\_\_oai\_logTTI():window.\_\_oai\_SSR\_TTI=window.\_\_oai\_SSR\_TTI||Date.now()})) Tools Chat

# english


# ChatGPT said:
# Sure! Here’s the Object-Oriented Programming (OOPs) explanation in English with the same Python examples — easy and beginner-friendly:

# 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
# 🔹 2. Object
# An object is a real instance of a class — created from that blueprint and stored in memory.

# python
# Copy
# Edit
# Creating objects
student1 = Student("Rahul", 18)
student2 = Student("Asha", 19)

# Calling a method using object
student1.introduce()
student2.introduce()
# 🔹 3. Inheritance
# Inheritance allows one class to reuse the properties and methods of another class.

# python
# Copy
# Edit
class Person:
    def speak(self):
        print("I can speak!")

# Student inherits from Person
class Student(Person):
    def study(self):
        print("I can study!")

s1 = Student()
s1.speak()   # Inherited from Person
s1.study()   # Defined in Student
# 🔹 4. Encapsulation
# Encapsulation means hiding internal details and only exposing what is necessary — like locking private data and accessing it through methods.

# python
# Copy
# Edit
class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(1000)
print(account.get_balance())  # Access through method
# 🔹 5. Polymorphism
# Polymorphism means "many forms" — the same method name behaves differently in different classes.

# python
# Copy
# Edit
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

# Polymorphism in action
for animal in (Cat(), Dog()):
    animal.sound()
# ✅ Summary Table
# Concept	What It Means	Python Keyword/Usage
# Class	Blueprint or template for objects	class
# Object	Instance of a class	obj = ClassName()
# Inheritance	One class reuses features of another class	class Child(Parent)
# Encapsulation	Hiding private data	__private_variable
# Polymorphism	Same method, different behavior	obj.method() in different classes

