# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

# Solution:

class Student:
    def __init__(self, name, marks):
        self.name =  name
        self.marks = marks
    def display(self):
            print(f"Name: {self.name}, and  Student Marks is: {self.marks} ")



Student1 = Student("Hasnain Abass",96 )
Student1.display()
        
Student2 = Student("Ali Khan", 85)
Student2.display()

Student3 = Student("Sara Ali", 90)
Student3.display()