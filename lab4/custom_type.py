from dataclasses import dataclass
from typing import List, Callable

Equation = Callable[[float], float]

@dataclass
class Result:
    is_calculate: bool
    coefficients: List[float]

@dataclass
class Fun:
    description: str
    f: Equation
    short_description: str
