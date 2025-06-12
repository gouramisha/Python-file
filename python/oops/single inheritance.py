class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def display(self):
        print("Child")

obj = Child()
obj.show()     # Inherited from Parent
obj.display()  # Defined in Child