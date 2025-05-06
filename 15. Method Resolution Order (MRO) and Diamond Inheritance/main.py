
# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

# solution:

class A :
    def __init__(self):
        pass
    
    def show(self):
        print("A's show() method")

class B(A) :
    def __init__(self):
        super().__init__()

    def show(self):
        print("B's show() method")

class C(A):
    def __init__(self):
        super().__init__()

    def show(self):
        print("C's show() method")

class D(B , C):
    def __init__(self):
        super().__init__()

    def show(self):
        print("D's show() method")
        super().show()
   


d = D()
d.show()