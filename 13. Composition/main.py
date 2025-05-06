# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

# solution

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.engine_type} engine started."
        return "Engine is already running."
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            return "Engine stopped."
        return "Engine is already off."
    
    def get_status(self):
        return "Running" if self.is_running else "Off"


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  
    
    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"
    
    def stop(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"
    
    def check_engine_status(self):
        return f"Engine status: {self.engine.get_status()}"



v6_engine = Engine("V6")


my_car = Car("Toyota", "Camry", v6_engine)


print(my_car.start()) 
print(my_car.check_engine_status())
print(my_car.stop())
print(my_car.check_engine_status())




    



        

