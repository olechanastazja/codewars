import math
import abc
from functools import total_ordering


@total_ordering
class Shape(abc.ABC):

    @property
    @abc.abstractmethod
    def area(self):
        pass

    def __gt__(self, other):
        return self.area > other.area

    def __repr__(self):
        return f"{self.__class__.__name__}({round(self.area, 2)})"


class Square(Shape):

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side * self.side


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def area(self):
        return self.height * self.base / 2


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.radius * self.radius * math.pi


class CustomShape(Shape):

    def __init__(self, area):
        self._area = area

    @property
    def area(self):
        return self._area


side = 1.1234
radius = 1.1234
base = 5
height = 2

# All classes must be subclasses of the Shape class

shapes = [Square(side), Circle(radius), Triangle(base, height)]
shapes.sort()
