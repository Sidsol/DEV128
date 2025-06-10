# Assignment: rectangle.py
# Class: DEV 128
# Date: 04/30/2025
# Author: Jonah Martinez
# Description: Defines a rectrangle class and a point class. The rectangle class has properties for width, height, area, and perimeter. It also has methods to translate the rectangle and check its properties.
# The point class has properties for x and y coordinates and a method to translate the point.
# This program is mean to help understand the use of classes and objects in Python.


from dataclasses import dataclass


class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    # Properties for x and y coordinates
    # These properties are read-only, meaning they can only be accessed, not modified directly
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # Method to move the x and y coordinates of the Point object
    def translate(self, dx, dy):
        self.__x += dx
        self.__y += dy
        return


class Rectangle:
    # Default values for width and height
    DEFAULT_WIDTH = 1
    DEFAULT_HEIGHT = 1

    # Class variable to keep track of the number of Rectangle objects created
    rectangleCount = 0

    def __init__(self, topLeft: Point, width: int, height: int):
        # Increment the rectangle count each time a new Rectangle object is created
        Rectangle.rectangleCount += 1
        self.__topLeft = topLeft

        if width > 0:
            self.__width = width
        else:
            print(
                "Width cannot be negative or zero. Setting it to the default value of 1"
            )
            self.width = Rectangle.DEFAULT_WIDTH

        if height > 0:
            self.__height = height
        else:
            print(
                "Height cannot be negative or zero. Setting it to the default value of 1"
            )
            self.height = Rectangle.DEFAULT_HEIGHT

    # Getters and setters for the topLeft, width, and height properties
    @property
    def topLeft(self):
        return self.__topLeft

    @topLeft.setter
    def topLeft(self, newTopLeft: Point):
        self.__topLeft = newTopLeft

    @property
    def width(self):
        return self.__width

    # Validates that the new width is greater than 0 before setting it
    # If the new width is not valid, it prints an error message and does not change the width
    @width.setter
    def width(self, newWidth: int):
        if newWidth > 0:
            self.__width = newWidth
        else:
            print("Width cannot be negative or zero.")

    @property
    def height(self):
        return self.__height

    # Validates that the new height is greater than 0 before setting it
    # If the new height is not valid, it prints an error message and does not change the height
    @height.setter
    def height(self, newHeight: int):
        if newHeight > 0:
            self.__height = newHeight
        else:
            print("Height cannot be negative or zero.")

    # Read only property for botttomLeft, area and perimeter
    # Returns a Point object representing the bottom right corner of the Rectangle
    @property
    def bottomRight(self):
        return Point(self.__topLeft.x + self.__width, self.__topLeft.y + self.__height)

    # Returns the area of the rectangle calculated using the width and height property values.
    @property
    def area(self):
        return self.__width * self.__height

    # Returns the perimeter of the rectangle calculated using the width and height property values.
    @property
    def perimeter(self):
        return 2 * (self.__width + self.__height)

    # Method to move the rectangle by a specified distance in the x and y directions
    # It uses the translate method of the Point class to move the top left corner of the rectangle.
    def translate(self, dx, dy):
        self.__topLeft.translate(dx, dy)
        return
