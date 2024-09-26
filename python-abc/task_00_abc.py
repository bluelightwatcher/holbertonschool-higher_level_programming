#!/usr/bin/python3
""" Module creates abstract class"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class

    Method:
        sound: represent the animal's sound
    """

    @abstractmethod
    def soundi(self):
        pass


class Dog(Animal):
    """Subclass of Animal

    Method:
        sound: implements the sound of the animal instance
    """

    def __init__(self):
        pass

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Subclass of Animal

    Method:
        sound: implements the sound of the animal instance
    """

    def __init(self):
        pass

    def sound(self):
        return "Meow"
