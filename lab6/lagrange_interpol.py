from typing import List, Callable


class InvalidElementsError(Exception):
    pass

class LagrangeInterpolation:

    def __init__(self, x_interpolation_units: List[float], y_interpolation_units: List[float]):
        self.y_units, self.x_units = [], []
        self.set_units(x_interpolation_units, y_interpolation_units)
        self.coefficient = []

    def set_units(self, x_interpolation_units: List[float], y_interpolation_units: List[float]):
        if len(y_interpolation_units) != len(x_interpolation_units):
            raise InvalidElementsError("Количество абсцисс и ординат не совпадает")
        self.x_units = x_interpolation_units.copy()
        self.y_units = y_interpolation_units.copy()

    def calc_coefficient(self, point: float, num_coefficient: int):
        produce = 1
        for i in range(len(self.x_units)):
            if i != num_coefficient:
                produce *= point - self.x_units[i]
                produce /= self.x_units[num_coefficient] - self.x_units[i]
        if len(self.x_units) >= 2:
            return produce
        else:
            raise InvalidElementsError("Мало точек!")

    def calc_coefficients(self, point: float):
        self.coefficient = []
        for i in range(len(self.x_units)):
            self.coefficient.append(self.calc_coefficient(point=point, num_coefficient=i))

    def calc_lagrange_by_point(self, point: float):
        self.calc_coefficients(point)
        s = 0
        for i in range(len(self.x_units)):
            s += self.coefficient[i] * self.y_units[i]
        return s
