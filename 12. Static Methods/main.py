# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

#  solution

class TempratureConvertor:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    


print(TempratureConvertor.celsius_to_fahrenheit(30))