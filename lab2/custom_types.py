from typing import Annotated, Callable, Literal
import numpy as np
import numpy.typing as npt

from dataclasses import dataclass


Vector = Annotated[npt.NDArray[np.double], Literal["N"]]
Array2D = Annotated[npt.NDArray[np.double], Literal["N", "N"]]

Equation = Callable[[int, int], float]

@dataclass
class SystemSolution:
    roots: Vector
    iterations: int

@dataclass
class EquationSolution:
    root: float
    iterations: int

@dataclass
class Fun:
    description: str
    f_x: Equation
    g_x_for_iter: Equation
