# Parent class
class Vehicle:
    def start(self):
        print("Vehicle chalu ho gaya!")

# Child class
class Car(Vehicle):
    def drive(self):
        print("Car chal rahi hai!")

# Use
c = Car()
c.start()  # Inherited from Vehicle
c.drive()  # Car ka apna method
