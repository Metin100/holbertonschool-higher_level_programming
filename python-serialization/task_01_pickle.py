#!/usr/bin/python3
"""Module containing pickle module and CustomObject"""


class CustomObject:
    """The CustomObject class"""
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Initialization of instance"""
        print(f'Name: {self.name}\nAge: {self.age}\n\
              Is Student: {self.is_student}')

    def serialize(self, filename):
        """Serialize filename"""
        import pickle

        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Exception: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Method to deserialize the Object from file"""
        import pickle

        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f'Exception {e}')
            return None
