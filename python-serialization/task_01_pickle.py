#!/usr/bin/env python3
""" use pickle to serialize and deserialize"""

import pickle  # Corrected import


class CustomObject:
    
    """
        Class to store student details
    """

    def __init__(self, name, age, is_student):
        """Constructor"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):     
        """Display"""
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """Serialize into binary file"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Class method to do binary file to object conversion"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None
