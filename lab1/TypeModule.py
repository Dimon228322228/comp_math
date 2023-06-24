from typing import Literal, Annotated

import numpy as np
import numpy.typing as npt
from dataclasses import dataclass

Vector = Annotated[npt.NDArray[np.double], Literal["N"]]
Array2D = Annotated[npt.NDArray[np.double], Literal["N", "N"]]

@dataclass
class MatrixParams:
    size: int
    accuracy: float


@dataclass
class InputData:
    params: MatrixParams
    matrix: Array2D
    vec_free_val: Vector


@dataclass
class Results:
    matrix: Array2D
    vec_b: Vector
    roots: Vector
    amount_iter: int
    inaccuracy: Vector
