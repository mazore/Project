import math

class Vector2:
    """Represents a 2d vector with x and y components. This class is used to represent positions,
    velocities, and more in the simulation
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        """Length of the vector"""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    length = magnitude = __abs__

    def magnitude_squared(self):
        """Used to avoid costly square root operation"""
        return self.x ** 2 + self.y ** 2

    def __getitem__(self, index):
        """Used to access the x and y components of the vector using the index operator"""
        if index == 'x' or index == 0:
            return self.x
        if index == 'y' or index == 1:
            return self.y
        raise IndexError("Invalid subscript " + str(index) + " to Vector2")

    def __setitem__(self, index, value):
        """Used to set the x and y components of the vector using the index operator"""
        if index == 'x' or index == 0:
            self.x = value
        elif index == 'y' or index == 1:
            self.y = value
        else:
            raise IndexError("Invalid subscript " + str(index) + " to Vector2")

    def normalize(self):
        """Scales the vector to have length 1"""
        l = self.magnitude()
        if l:
            self.x = self.x / l
            self.y = self.y / l

    def normalized(self):
        """Returns a version of the vector with length 1"""
        length = self.magnitude()
        if length:
            return Vector2(self.x / length, self.y / length)
        return Vector2(0, 0)

    def dot(self, other):
        """Takes the dot product of this vector and another vector"""
        return self.x * other.x + self.y * other.y

    def distance(self, other):
        """Finds the distance, assuming vectors represent some position"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def tuple(self):
        return (self.x, self.y)

    def intTuple(self):
        """Used for drawing the vector as a position in pygame"""
        return (int(self.x), int(self.y))

    def __copy__(self):
        """Creates a copy of the vector"""
        return Vector2(self.x, self.y)

    def __eq__(self, other):
        """Tests equality of the vectors"""
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """Adds two vectors"""
        return Vector2(self.x + other.x, self.y + other.y)
    __radd__ = __add__

    def __sub__(self, other):
        """Subtracts the other vector from this one"""
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Multiplies the vector by a scalar"""
        assert isinstance(other, (int, float))
        return Vector2(self.x * other, self.y * other)
    __rmul__ = __mul__

    def __truediv__(self, other):
        """Divides the vector by a scalar"""
        assert isinstance(other, (int, float))
        return Vector2(self.x / other, self.y / other)

    def __floordiv__(self, other):
        """Divides the vector by a scalar using floor division"""
        assert isinstance(other, (int, float))
        return Vector2(self.x // other, self.y // other)

    def __neg__(self):
        """Makes the vector negative"""
        return Vector2(-self.x, -self.y)

    def __pos__(self):
        """Positive version of the vector"""
        return Vector2(self.x, self.y)

    def __repr__(self):
        return "Vector2("+str(self.x)+", "+str(self.y)+")"
