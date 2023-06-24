import numpy as np

from TypeModule import Results
from matrixAction import convert_to_dominant


def can_solve(A):
    A_abs = np.abs(A)
    flag = True
    for i, x in enumerate(A_abs):
        if not 2 * x[i] > np.sum(A_abs[i]):
            flag = False
    return flag


def matrix_resolve(A, b, x0, tol=1e-6) -> Results:
    if not can_solve(A):
        res = convert_to_dominant(A, b)
        A = res[0]
        b = res[1]
    D_inv = np.diag(np.reciprocal(np.diag(A)))
    C = np.eye(A.shape[0]) - np.matmul(D_inv, A)
    c = np.matmul(D_inv, b)
    x = x0
    iteration: int = 0
    while True:
        x_next = np.matmul(C, x) + c
        iteration += 1
        inaccuracy = np.abs(x_next - x)
        if np.allclose(x, x_next, atol=tol, rtol=0.0):
            return Results(matrix=A, vec_b=b, roots=x_next, amount_iter=iteration, inaccuracy=inaccuracy)
        x = x_next


def per_element_resolve(A, b, x0, tol=1e-6) -> Results:
    if not can_solve(A):
        res = convert_to_dominant(A, b)
        A = res[0]
        b = res[1]
    D = np.diag(A)
    iterations: int = 0
    x = x0

    while True:
        x_next = np.zeros_like(x)
        for i, x_i in enumerate(x):
            f_i = np.sum(A[i] * x) - b[i]
            x_next[i] = x[i] - f_i / D[i]
        iterations += 1
        inaccuracy = np.abs(x_next - x)
        if np.allclose(x, x_next, atol=tol, rtol=0.0):
            return Results(matrix=A, vec_b=b, roots=x_next, amount_iter=iterations, inaccuracy=inaccuracy)
        x = x_next
