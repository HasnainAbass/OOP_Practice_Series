# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# solution

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject


class Person(Teacher):
    def __init__(self, name, subject):
        super().__init__(name, subject)
        self.name = name
        self.subject = subject

    def display(self):
        print(f"Name:MR/MS {self.name} and his Subject is: {self.subject}")


student1 = Person("Hasnain Abass", "Mathematics")
student1.display()
student2 = Person("Ali", "Physics")
student2.display()