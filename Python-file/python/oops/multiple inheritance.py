# Parent class 1
class Father:
    def skills(self):
        print("Father: Gardening, Programming")

# Parent class 2
class Mother:
    def skills(self):
        print("Mother: Cooking, Art")

# Child class
class Child(Father, Mother):
    def own_skill(self):
        print("Child: Dancing")

# Create object of Child
c = Child()
c.skills()      # Will call Father’s method (due to method resolution order)
c.own_skill()
