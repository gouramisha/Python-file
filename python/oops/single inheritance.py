class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def display(self):
        print("Child")

obj = Child()
obj.show()     # Inherited from Parent
obj.display()  # Defined in Child

class Vehicle:
    def start_engine(self):
        print("Engine started.")

class Car(Vehicle):  # Car inherits from Vehicle
    def play_music(self):
        print("Playing music in the car.")

# Create object of Car class
my_car = Car()

# Call methods
my_car.start_engine()  # Inherited from Vehicle
my_car.play_music()    # Defined in Car


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat