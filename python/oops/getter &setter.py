class Student:
    def __init__(self):
        self._name = "Chintu"

    @property
    def name(self):       # 👈 Getter
        return self._name

    @name.setter
    def name(self, value):  # 👈 Setter
        self._name = value

s = Student()

print(s.name)       # "Chintu"  ➜ automatically runs getter

s.name = "Pintu"    # ➜ automatically runs setter

print(s.name)       # "Pintu"