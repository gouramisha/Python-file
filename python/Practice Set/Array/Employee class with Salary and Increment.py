class Employee:
    def __init__(self, salary):
        self._salary = salary
        self._increment = 0.1  # Default increment 10%

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        if self._salary > 50000:
            self._increment = 0.2  # 20% for high salary
        else:
            self._increment = value  # set passed value

    @property
    def salaryAfterIncrement(self):
        return self._salary + (self._salary * self._increment)
