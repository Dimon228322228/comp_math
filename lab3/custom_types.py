from typing import Callable

from dataclasses import dataclass

Equation = Callable[[int, int], float]

@dataclass
class IntegralSolution:
    has_solve: bool
    sum: float
    partition: int
    err: str

@dataclass
class Fun:
    description: str
    f_x: Equation