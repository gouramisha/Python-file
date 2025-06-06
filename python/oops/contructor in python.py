class Student:
    def __init__(self, name, age):
        self.name = name    # object ka name set karo
        self.age = age      # object ki age set karo

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Object banao — constructor apne aap chalega
s1 = Student("Raju", 15)
s1.show()
