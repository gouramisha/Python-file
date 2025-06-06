# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Another Child class
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Create objects
dog = Dog()
cat = Cat()

# Using parent class method
dog.speak()
cat.speak()

# Using child class methods
dog.bark()
cat.meow()
