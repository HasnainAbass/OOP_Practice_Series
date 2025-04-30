# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

# Solution:

class Car():
    def __init__(self):
        pass
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f"The {self.brand} Car is Starting ..............")
 



Car1 = Car("Toyota")
print(Car1.brand)  # Accessing the public variable
Car1.start() 


Car2 = Car("Honda")
print(Car2.brand)
Car2.start()  
