class Employee:
    def __init__(self, salary, increment):
        self._salary = salary
        self._increment = increment

    @property
    def salaryAfterIncrement(self):
        return self._salary + (self._salary * self._increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self._increment = ((new_salary - self._salary) / self._salary) * 100


# Example usage
emp = Employee(50000, 10)
print("Salary after increment:", emp.salaryAfterIncrement)

emp.salaryAfterIncrement = 60000
print("New Increment %:", emp._increment)
