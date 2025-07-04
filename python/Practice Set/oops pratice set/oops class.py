class Programmer:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show(self):
        print(f"Name: {self.name}, Company: {self.company}")

# Example
p1 = Programmer("Alice", "Microsoft")
p2 = Programmer("Bob", "Microsoft")
p1.show()
p2.show()
