# Parent Class
class Vehicle:
    def show_info(self):
        print("This is a vehicle.")

# Child Class 1
class Car(Vehicle):
    def car_info(self):
        print("This is a car.")

# Child Class 2
class Bike(Vehicle):
    def bike_info(self):
        print("This is a bike.")

# Child Class 3
class Truck(Vehicle):
    def truck_info(self):
        print("This is a truck.")

# Create objects
car = Car()
bike = Bike()
truck = Truck()

# Call methods
car.show_info()      # Inherited from Vehicle
car.car_info()       # Own method

bike.show_info()     # Inherited from Vehicle
bike.bike_info()     # Own method

truck.show_info()    # Inherited from Vehicle
truck.truck_info()   # Own method
