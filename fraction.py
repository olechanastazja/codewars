# Something goes Here ...
from math import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    def __eq__(self, other):
        return self.top * other.bottom == other.top * self.bottom

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Wrong type - Fraction expected")
        new_denominator = self.bottom * other.bottom
        nominator1 = self.top * other.bottom
        nominator2 = other.top * self.bottom
        new_nominator = nominator1 + nominator2

        x = gcd(new_nominator, new_denominator)
        self.top = int(new_nominator / x)
        self.bottom = int(new_denominator / x)
        return self

    def __repr__(self):
        return f"{self.top}/{self.bottom}"
