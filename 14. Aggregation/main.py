# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# solution

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
    def display(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")


class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  

    def display(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  


emp = Employee(101, "Hasnain Abass") 
dept = Department("Computer Science", emp)  
dept.display()

