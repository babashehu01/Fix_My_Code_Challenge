#!/usr/bin/python3

class Square():
    
    side = 0

    def __init__(self, side, *args, **kwargs):
        self.side = side

    def area_of_my_square(self):
        """ Area of the square """
        return self.side * self.side

    def PerimeterOfMySquare(self):
        return self.side * 4

    def __str__(self):
        return "{}".format(self.side)

if __name__ == "__main__":

    s = Square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())
