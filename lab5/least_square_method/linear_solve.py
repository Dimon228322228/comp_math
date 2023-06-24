from typing import List


def convert_to_matrix(c: List[float], len_b: int):
    matrix = []
    first_coefficient = 0
    for i in range(len_b):
        row = []
        for j in range(len_b):
            row.append(c[first_coefficient + j])
        matrix.append(row)
        first_coefficient += 1
    return matrix


def gauss(c: List[float], b: List[float]):
    A = convert_to_matrix(c, len(b))
    """Solve A*X = B using the Gauss elimination method"""


    n = len(A)
    s = [0.0] * n
    X = [0.0] * n

    p = [i for i in range(n)]
    for i in range(n):
        s[i] = max(abs(x) for x in A[i])

    for k in range(n - 1):
        # select j>=k so that
        # |A[p[j]][k]| / s[p[i]] >= |A[p[i]][k]| / s[p[i]] for i = k,k+1,...,n
        j = k
        ap = abs(A[p[j]][k]) / s[p[j]]
        for i in range(k + 1, n):
            api = abs(A[p[i]][k]) / s[p[i]]
            if api > ap:
                j = i
                ap = api

        if j != k:
            p[k], p[j] = p[j], p[k]  # Swap values

        for i in range(k + 1, n):
            z = A[p[i]][k] / A[p[k]][k]
            A[p[i]][k] = z
            for j in range(k + 1, n):
                A[p[i]][j] -= z * A[p[k]][j]

    for k in range(n - 1):
        for i in range(k + 1, n):
            b[p[i]] -= A[p[i]][k] * b[p[k]]

    for i in range(n - 1, -1, -1):
        X[i] = b[p[i]]
        for j in range(i + 1, n):
            X[i] -= A[p[i]][j] * X[j]
        X[i] /= A[p[i]][i]

    return X


def kramer_solve(c: List[float], b: List[float]):
    matrix = convert_to_matrix(c, len(b))
    n = len(matrix)

    determinant = calculate_determinant(matrix)
    if determinant == 0:
        raise ValueError("Матрица системы вырождена. Метод Крамера не применим.")

    solutions = []

    for i in range(n):
        matrix_copy = [row.copy() for row in matrix]
        for j in range(n):
            matrix_copy[j][i] = b[j]
        det_i = calculate_determinant(matrix_copy)
        solutions.append(det_i / determinant)

    return solutions


def calculate_determinant(matrix):
    n = len(matrix)

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0

    for j in range(n):
        submatrix = []

        for i in range(1, n):
            row = matrix[i][:]
            row.pop(j)
            submatrix.append(row)

        determinant += matrix[0][j] * calculate_determinant(submatrix) * (-1) ** j

    return determinant


if __name__ == "__main__":
    a = [[1, -2],
         [2, -3]]
    print(f"{calculate_determinant(a)}")
    b = [[1, 2, 3],
         [2, 3, 4],
         [4, 15, 6]]
    print(f'{calculate_determinant(b)}')
