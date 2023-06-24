import math
from typing import Tuple

from custom_types import IntegralSolution
from data import getFun


def is_invalid(f, val):
    return math.isnan(f(val)) or math.isinf(f(val))


def create_error_answer() -> IntegralSolution:
    return IntegralSolution(has_solve=False, sum=0, partition=0,
                            err="Функция имеет разрывы второго рода или не определена на данном интервале")


def try_add(f, s: float, x: float, coeff: float) -> Tuple[bool, float]:
    dx = 0.0000001
    try:
        if is_invalid(f, x) and not is_invalid(f, x + dx) and not is_invalid(f, x - dx):
            return True, s + (f(x + dx) + f(x - dx)) / 2 * coeff
        elif is_invalid(f, x):
            return False, s
        else:
            return True, s + coeff * f(x)
    except Exception as e:
        return False, s


def calculate_integral(a, b, num_f, tol=1e-6) -> IntegralSolution:
    try:
        f = getFun(num_f).f_x
    except ValueError as e:
        return IntegralSolution(has_solve=False, sum=0, partition=0, err=f"{e}")
    is_reverse: bool = a > b
    if is_reverse:
        a, b = b, a
    n = 100
    old_sum = 0

    while True:
        sum = 0
        h = (b - a) / n

        for i in range(1, n):
            x = a + i * h
            is_OK, sum = try_add(f, sum, x, 2) if i % 2 == 0 else try_add(f, sum, x, 4)
            if not is_OK:
                return create_error_answer()

        for i in [a, b]:
            is_OK, sum = try_add(f, sum, i, 1)
            if not is_OK:
                return create_error_answer()

        sum = h / 3 * sum
        if abs(sum - old_sum) > tol:
            old_sum = sum
            n *= 2
            continue
        return IntegralSolution(has_solve=True, sum=-sum if is_reverse else sum, partition=n, err="")
