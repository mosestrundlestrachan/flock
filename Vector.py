from math import sqrt

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float) -> "Vector":
        return Vector(self.x / scalar, self.y / scalar)

    def __iter__(self):
        yield self.x
        yield self.y

    def length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self) -> "Vector":
        length = self.length()
        if length != 0:
            return self / length
        return Vector(0, 0)