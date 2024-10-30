#!/usr/bin/bash
"""Module serializes and deserializes an object using pickle module"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject with name, age, and is_student attributes.
        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of CustomObject to a file.

        Parameters:
        filename (str): The filename where the serialized object will be saved.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object has been serialized and saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while serializing the object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a file.

        Parameters:
        filename (str): The filename from which to load the serialized object.

        Returns:
        CustomObject: An instance of CustomObject loaded from the file.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            print(f"Object has been deserialized from {filename}.")
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"An error occurred during deserialization: {e}")
            return None
