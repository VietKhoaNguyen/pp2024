# pw4/person.py
class Person:
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def input(self):
        self.__name = input("Enter name: ")
        self.__dob = input("Enter Date of Birth (DD/MM/YYYY): ")

    def __str__(self):
        return f"Name: {self.__name}, DoB: {self.__dob}"
