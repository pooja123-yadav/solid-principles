"""
https://medium.com/@samyakmoon855/liskovs-substitution-principle-b1d415a5d15f

https://realpython.com/solid-principles-python/

this principle has been a fundamental part of object-oriented programming. The principle states that:

A sub-class must be substitutable for its super-class.

The aim of this principle is to ascertain that a sub-class can assume the place of its super-class without errors. 
If the code finds itself checking the type of class then, it must have violated this principle.

This principle exist so we can unnderstand inherit properly.
It happens may be your code : works, serves the requirement correctly but conceptually wrong
If we inherit the classes in a correct way then this principle will not be violated but if we inherited in the 
wrong way then it violate the Liskov substitution principle

If a function takes an instance of a class. That same function also be able to take the instance of derived
class from that class.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value


square = Square(5)
vars(square)
# {'width': 5, 'height': 5}

square.width = 7
vars(square)
# {'width': 7, 'height': 7}

square.height = 9
vars(square)
# {'width': 9, 'height': 9}