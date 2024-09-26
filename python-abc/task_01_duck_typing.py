#!/usr/bin/python3
"""This module defines an abstract class Shape and its concrete subclasses 
Circle and Rectangle. Each shape class implements methods to calculate 
area and perimeter, providing a structure for polymorphic behavior.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract class representing a geometric shape.

    This class defines the interface for shapes with methods to calculate 
    area and perimeter, which must be implemented by subclasses.

    Methods:
        area() -> float: Calculate and return the area of the shape.
        perimeter() -> float: Calculate and return the perimeter of the shape.
    """

    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        This method must be overridden by subclasses to provide 
        the specific area calculation.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.

        This method must be overridden by subclasses to provide 
        the specific perimeter calculation.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """Subclass of Shape representing a circle.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        area() -> float: Calculate and return the area of the circle.
        perimeter() -> float: Calculate and return the perimeter of the circle.
    """

    def __init__(self, radius):
        """Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate and print the area of the circle.

        Returns:
            float: The area of the circle, calculated using the formula 
            π * radius^2.
        """
        area_value = 3.14159 * (self.radius ** 2)
        print(f"Area: {area_value}")
        return area_value

    def perimeter(self):
        """Calculate and print the perimeter of the circle.

        Returns:
            float: The perimeter of the circle, calculated using the formula 
            2 * π * radius.
        """
        perimeter_value = 2 * 3.14159 * self.radius
        print(f"Perimeter: {perimeter_value}")
        return perimeter_value


class Rectangle(Shape):
    """Subclass of Shape representing a rectangle.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        area() -> float: Calculate and return the area of the rectangle.
        perimeter() -> float: Calculate and return the perimeter of the rectangle.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate and print the area of the rectangle.

        Returns:
            float: The area of the rectangle, calculated using the formula 
            width * height.
        """
        area_value = self.width * self.height
        print(f"Area: {area_value}")
        return area_value

    def perimeter(self):
        """Calculate and print the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle, calculated using the formula 
            2 * (width + height).
        """
        perimeter_value = (self.width * 2) + (self.height * 2)
        print(f"Perimeter: {perimeter_value}")
        return perimeter_value

