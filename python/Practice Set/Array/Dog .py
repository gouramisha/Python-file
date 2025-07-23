#  Animal → Pets → Dog with bark()
class Animals:
    def __init__(self, name):
        self.name = name

class Pets(Animals):
    def __init__(self, name):
        super().__init__(name)

class Dog(Pets):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        return f"{self.name} says Woof!"
