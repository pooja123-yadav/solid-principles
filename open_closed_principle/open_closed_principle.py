"""
Open-Closed Principle
Software entities(Classes, modules, functions) should be open for extension, not modification.
"""        

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2

class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.calculate_area()

rect = Rectangle(5, 10)
circle = Circle(7)
triangle = Square(6)

calculator = AreaCalculator()
print("Rectangle Area:", calculator.calculate_area(rect))      # 50
print("Circle Area:", calculator.calculate_area(circle))        # 153.86
print("Triangle Area:", calculator.calculate_area(triangle))    # 24.0



"""
 This update closes the class to modifications. Now you can add new shapes to your class design without
 the need to modify Shape. In every case, you’ll have to implement the required interface, which also 
 makes your classes polymorphic.
"""
