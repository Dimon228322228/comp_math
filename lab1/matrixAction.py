import numpy as np

from TypeModule import Vector, Array2D


class NoDiagonallyDominantException(Exception):
    pass


def convert_to_dominant(matrix: Array2D, b: Vector) -> (Array2D, Vector):
    abs_m = np.abs(matrix)
    max_per_row = np.amax(abs_m, axis=1)
    maxi_per_row = np.argmax(abs_m, axis=1)

    if np.all(max_per_row > (np.sum(abs_m, axis=1) - max_per_row)) and np.array_equal(np.sort(maxi_per_row), np.arange(len(maxi_per_row))):
        return matrix[maxi_per_row, :], np.sum(np.diag(b)[maxi_per_row, :], axis=1)
    else:
        raise NoDiagonallyDominantException("Невозможно привести матрицу к диагональному преобладанию")


def generate_random_matrix(size: int):
    matrix = np.random.rand(size, size)
    np.fill_diagonal(matrix, np.diag(matrix) + size)
    return matrix


def generate_random_vec_free_val(size: int):
    return np.random.rand(size)