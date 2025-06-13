class A:  # Base Class
    def show_A(self):
        print("I am from Class A")

class B(A):  # Derived from A
    def show_B(self):
        print("I am from Class B")

class C(B):  # Derived from B
    def show_C(self):
        print("I am from Class C")

# Creating object of Class C
obj = C()

obj.show_A()  # Inherited from Class A
obj.show_B()  # Inherited from Class B
obj.show_C()  # Defined in Class C
