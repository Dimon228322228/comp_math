import math
from typing import List


class InvalidPointError(Exception):
    pass


class ChebyshevInterpolation:

    def __init__(self, a: float, b: float):
        self.a, self.b = a, b
        self.scaler = Scaler(a, b)

    def get_root_by_section(self, degree_polynom: int) -> List[float]:
        k = 1
        roots = []
        while k <= degree_polynom:
            roots.append(math.cos((2 * k - 1) * math.pi / (2 * degree_polynom)))
            k += 1
        for i in range(len(roots)):
            roots[i] = self.scaler.from_normal_section(roots[i])
        roots = sorted(roots)
        return roots


class Scaler:

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def to_normal_section(self, point: float) -> float:
        if point > self.b or point < self.a:
            raise InvalidPointError("Точка не входит в интервал [a, b]")
        return (2 * point - self.a - self.b) / (self.b - self.a)

    def from_normal_section(self, point: float) -> float:
        if point > 1 or point < -1:
            raise InvalidPointError("Точка не входит в интервал [-1, 1]")
        return ((self.b - self.a) * point + self.a + self.b) / 2
