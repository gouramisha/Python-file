class Student:
    # Static variable
    school_name = "Gyan Deep School"

    def __init__(self, name, roll):
        self.name = name        # Instance variable
        self.roll = roll        # Instance variable

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"School: {Student.school_name}")  # Access static variable


# Creating objects
s1 = Student("Riya", 101)
s2 = Student("Amit", 102)

# Show details
s1.show_details()
print("----")
s2.show_details()
