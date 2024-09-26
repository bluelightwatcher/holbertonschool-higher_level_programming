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

    Attribute:
        radius: is the radius of the circle

    Method:
       area: is the area of a circle
       perimeter: is the perimeter of a circle
    """

    def __init__(self, radius):
        """
        Initialize a circle instance

        Args:
            radius: radius of the circle
        """
        self.radius = radius

    def area(self):
        """prints area of a circle
        """
        self.area = 3.14159 * (self.radius ** 2)
        print(f"Area : {self.area}")

    def perimeter(self):
        """prints perimeter of a circle
        """
        self.perimeter = 2 * 3.14159 * self.radius
        print(f"Perimeter : {self.perimeter}")


class Rectangle(Shape):
    """Subclass of Shape

    Attribute:
        width: is the width of the rectangle
        height: is the height of the rectangle

    Method:
       area: is the area of a rectangle
       perimeter: is the perimeter of a rectangle
    """

    def __init__(self, width, height):
        """
        creates an instance of a rectangle

        Args:
            width: is the rectangle width
            height: is the rectangle height
        """

        self.width = width
        self.height = height

    def area(self):
        """prints area of a rectangle
        """
        self.area = self.width * self.height
        print(f"Area : {self.area}")

    def perimeter(self):
        """prints perimeter of a rectangle
        """
        self.perimeter = (self.width * 2) + (self.height * 2)
        print(f"Perimeter : {self.perimeter}")


def shape_info(Shape_obj):
    """method calls area and perimeter method
    relies on duck typing

    Args:
        Shape_obj (Shape): is an instance of an object derived of Shape

    """
    Shape_obj.area()
    Shape_obj.perimeter()
