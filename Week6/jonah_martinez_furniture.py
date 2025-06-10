# Assignment: Furniture Inheritance
# Class: DEV 128
# Date: 05/21/2025
# Author: Jonah Martinez
# Description: This program a base class Furniture and two derived classes
# Table and Bed. It demonstrates the use of inheritance in python.


# validate the weight is a positive integer
def validateWeight(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"Weight must be positive")
    return value


class FurnitureGallery:
    def __init__(self):
        self.__furnList: list = []  # private list of furniture

    def addFurniture(self, furniture):
        # Validate that the furniture is an instance of Furniture or its subclasses
        if not isinstance(furniture, Furniture):
            raise ValueError(f"Invalid furniture type: {type(furniture)}")
        self.__furnList.append(furniture)

    # Uses the built-in sort function to sort the list of furniture
    # lambda function is used to sort by weight
    def sort(self):
        self.__furnList.sort(key=lambda x: x.weight)

    # Returns the list of furniture
    def __iter__(self):
        return iter(self.__furnList)


class Furniture:
    def __init__(self, weight):
        self.__weight: int = validateWeight(weight)

    # Returns a string representation of the object
    # This method is called when the object is printed
    def __str__(self):
        return f"Item Weight: {self.__weight} lbs"

    # __eq__ is used to compare two objects for equality
    def __eq__(self, other):
        if not isinstance(other, Furniture):
            return False
        return self.__weight == other.__weight

    # __lt__ is used to compare two objects for less than
    def __lt__(self, other):
        if not isinstance(other, Furniture):
            return False
        return self.__weight < other.__weight

    # __le__ is used to compare two objects for less than or equal to
    def __le__(self, other):
        if not isinstance(other, Furniture):
            return False
        return self.__weight <= other.__weight

    # __gt__ is used to compare two objects for greater than
    def __gt__(self, other):
        if not isinstance(other, Furniture):
            return False
        return self.__weight > other.__weight

    # __ge__ is used to compare two objects for greater than or equal to
    def __ge__(self, other):
        if not isinstance(other, Furniture):
            return False
        return self.__weight >= other.__weight

    # __ne__ is used to compare two objects for not equal
    def __ne__(self, other):
        if not isinstance(other, Furniture):
            return False
        return self.__weight != other.__weight

    @property
    def weight(self):
        return self.__weight

    # Set the weight of the object and validate it
    @weight.setter
    def weight(self, value):
        self.__weight = validateWeight(value)


class Table(Furniture):
    # Calls the base class constructor and passes the weight
    # Raises ValueError if wood is not a string
    def __init__(self, weight, wood):
        super().__init__(weight)
        if not isinstance(wood, str):
            raise ValueError(f"Wood must be of type string")
        self.wood = wood

    # Returns a string representation of the object by calling the base class __str__ method
    # and adding the wood type
    def __str__(self):
        return f"Table {super().__str__()} Made of: {self.wood}"


class Bed(Furniture):
    # Set of allowed bed sizes
    ALLOWED_SIZES = {"Twin", "Full", "Queen", "King"}

    # Calls the base class constructor
    # Raises ValueError if size is not in the allowed sizes
    def __init__(self, weight, size):
        super().__init__(weight)
        if size not in self.ALLOWED_SIZES:
            raise ValueError(f"Size must be one of {self.ALLOWED_SIZES}")
        self.size = size

    # Returns a string representation of the object by calling the base class __str__ method
    # and adding the bed size
    def __str__(self):
        return f"Bed {super().__str__()} Size: {self.size}"
