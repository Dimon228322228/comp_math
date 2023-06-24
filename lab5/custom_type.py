from dataclasses import dataclass
from typing import List, Callable

Equation = Callable[[float], float]
Equation_with_3_arg = Callable[[float, float, float], float]
x_data = List[float]
y_data = List[float]

@dataclass
class Result:
    is_calculate: bool
    coefficients: List[float]

@dataclass
class Fun:
    description: str
    f: Equation
    short_description: str
    analitic_solve_func: Equation_with_3_arg
