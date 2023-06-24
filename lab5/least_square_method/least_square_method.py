from typing import List

from custom_type import Result, Equation_with_3_arg
from least_square_method.linear_solve import kramer_solve, gauss


def generate_non_result():
    return Result(is_calculate=False, coefficients=[])


def least_square_solve(x_data: List[float], y_data: List[float], max_degree: int, func: Equation_with_3_arg, a, y_a) -> Result:
    c: List[float] = [0.0] * (max_degree * 2 + 1)
    b: List[float] = [0.0] * (max_degree + 1)
    try:
        for i in range(len(c)):
            c[i] = sum(func(x, y_a, a) ** i for x in x_data)
        for i in range(len(b)):
            b[i] = sum(y * func(x, y_a, a) ** i for x, y in zip(x_data, y_data))
    except Exception as e:
        return generate_non_result()
    try:
        coefficients = kramer_solve(c, b)
        return Result(is_calculate=True, coefficients=coefficients)
    except ValueError as e:
        try:
            coefficients = gauss(c, b)
            return Result(is_calculate=True, coefficients=coefficients)
        except Exception as e:
            return generate_non_result()
