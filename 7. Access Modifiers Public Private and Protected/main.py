# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

# solution


class Employee:
    def __init__(self , name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

obj = Employee("Hasnain Abass", 50000, "123-45-6789")
obj.display()