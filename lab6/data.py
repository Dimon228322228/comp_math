import math
from typing import Callable
from dataclasses import dataclass

Equation = Callable[[float], float]


@dataclass
class F:
    f: Equation
    descr: str


FUNCTIONS = [
    F(lambda x: 1 / (1 + 25 * x ** 2), "\t            1     \t\n"
                                       "\tf(x) = -----------\t\n"
                                       "\t        1 + 25x^2 \t\n"),
    F(lambda x: 1 / x, "\t        1 \t\n"
                       "\tf(x) = ---\t\n"
                       "\t        x \t\n"),
    F(lambda x: math.e ** x, "f(x) = e^x"),
    F(lambda x: math.sin(x), "f(x) = sin(x)"),
    F(lambda x: math.tan(x), "f(x) = tg(x)"),
    F(lambda x: 3*x - 4*x**2, "f(x) = 3x - 4x^2"),
    F(lambda x: 2*x**2 - 6*abs(x) - 3, "f(x) = 2*x^2 - 6|x| - 3"),
    F(lambda x: x**3 - 50 * x - 3, "f(x) =x^3- 50|x| - 3"),
]
