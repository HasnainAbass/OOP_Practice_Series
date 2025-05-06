# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


# solution

class logger:
    def __init__(self, name):
        self.name = name
        print(f"Object created with name: {self.name}")

    def __del__(self):
        print(f"Object destroyed with name: {self.name} ")    


s1 = logger("Logger1")
s2 = logger("Logger2")
print(s1)
print(s2)


