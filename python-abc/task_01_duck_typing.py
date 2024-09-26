#!/usr/bin/python3
""" Module creates abstract class"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class

    Method:
        area: represent the shape's area
        perimeter: is the shape's perimeter
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Subclass of Shape

    Method:
       area: is the area of a circle
       perimeter: is the perimeter of a circle
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.area = 3.14159 * (self.radius ** 2)
        print(f"Area : {self.area}")

    def perimeter(self):
        self.perimeter = 2 * 3.14159 * self.radius
        print(f"Perimeter : {self.perimeter}")


class Rectangle(Shape):
    """Subclass of Shape

    Method:
       area: is the area of a rectangle
       perimeter: is the perimeter of a rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        self.area = self.width * self.height
        print(f"Area : {self.area}")

    def perimeter(self):
        self.perimeter = (self.width * 2) + (self.height * 2)
        print(f"Perimeter : {self.perimeter}")


def shape_info(Shape):
    Shape.area()
    Shape.perimeter()
