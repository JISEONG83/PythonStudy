# Class examples

class Rectangle:
    count = 0

    # initializer
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def calcArea(self):
        area = self.width * self.height
        return area

    # static method
    #@staticmethod
    @classmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight

    # class method
    @classmethod
    #@staticmethod
    def printCount(cls):
        print(cls.count)

# using class & methods
square = Rectangle(5,5)
print(square)

rect1 = Rectangle(5,5)
rect2 = Rectangle(2,5)
rect1.printCount()

# instance creator & usage
r = Rectangle(2,3)

area = r.calcArea()
print('area = ', area)

r.width = 10
print('width = ', r.width)

# access the class variable
print(Rectangle.count)
print(r.count)

