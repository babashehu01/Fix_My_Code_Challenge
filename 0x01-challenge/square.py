#!/usr/bin/python3
"""Defines a class Square"""


class square():
    """Square claa"""    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """Initializing a Square class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of the Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the class"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """Creating a Square object"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
