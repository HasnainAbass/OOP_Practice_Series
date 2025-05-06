# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# solution:

def add_greeting(cls):
    def greet(self):
        return f"Hello MR . {self.name} from Decorator!" 
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self,name):
        self.name = name


p = Person("Hasnain")
print(p.greet())