import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #
    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    length = magnitude = __abs__

    def magnitude_squared(self):
        return self.x ** 2 + self.y ** 2

    def __getitem__(self, index):
        if index == 'x' or index == 0:
            return self.x
        if index == 'y' or index == 1:
            return self.y
        raise IndexError("Invalid subscript " + str(index) + " to Vector2")

    def __setitem__(self, index, value):
        if index == 'x' or index == 0:
            self.x = value
        elif index == 'y' or index == 1:
            self.y = value
        else:
            raise IndexError("Invalid subscript " + str(index) + " to Vector2")

    #
    def normalize(self):
        l = self.magnitude()
        if l:
            self.x = self.x / l
            self.y = self.y / l

    #
    def normalized(self):
        length = self.magnitude()
        if length:
            return Vector2(self.x / length, self.y / length)
        return Vector2(0, 0)

    #
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    #
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    #
    def tuple(self):
        return (self.x, self.y)

    def intTuple(self):  # Used for drawing the vector as a position in pygame
        return (int(self.x), int(self.y))

    #
    def __copy__(self):
        return Vector2(self.x, self.y)

    #
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    #
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    __radd__ = __add__

    #
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    #
    def __mul__(self, other):
        assert isinstance(other, (int, float))
        return Vector2(self.x * other, self.y * other)
    __rmul__ = __mul__

    #
    def __truediv__(self, other):
        assert isinstance(other, (int, float))
        return Vector2(self.x / other, self.y / other)

    def __floordiv__(self, other):
        assert isinstance(other, (int, float))
        return Vector2(self.x // other, self.y // other)

    #
    def __neg__(self):
        return Vector2(-self.x, -self.y)

    #
    def __pos__(self):
        return Vector2(self.x, self.y)

    #
    def __repr__(self):
        return "Vector2("+str(self.x)+", "+str(self.y)+")"
