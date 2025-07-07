class person:
    name = "Amisha"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
a.name = "Shubham"
a.occupation = "Accountant"
a.info()