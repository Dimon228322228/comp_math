from TypeModule import MatrixParams, InputData, Results
import numpy as np

from matrixAction import generate_random_matrix, generate_random_vec_free_val


class InvalidDataFormat(Exception):
    pass


def read_size_and_accuracy():
    size: int = int(input("Введите размерность системы: "))
    accuracy = float(input("Введите требуемую точность: "))
    return MatrixParams(size, accuracy)


def read_matrix(rows: int):
    a = np.zeros((rows, rows))
    print("Введите коэффициенты матрицы A построчно, символы в строке разделять пробелом:")
    for i in range(rows):
        a[i] = list(map(float, input().split()))
    return a


def read_vec_free_val():
    print("Введите значения вектора b в строку через пробел:")
    return np.array(list(map(float, input().split())))


def read_from_user():
    m_params = read_size_and_accuracy()
    size = m_params.size
    matrix = read_matrix(size)
    if (matrix.shape[0] != size or matrix.shape[1] != size):
        raise InvalidDataFormat("Размер матрицы A не соответствует введенному")
    vec_free_val = read_vec_free_val()
    if vec_free_val.shape[0] != size:
        raise InvalidDataFormat("Размер вектора b не соответствует введенному")
    return InputData(params=m_params, matrix=matrix, vec_free_val=vec_free_val)


def read_and_gen_random_matrix():
    m_params = read_size_and_accuracy()
    matrix = generate_random_matrix(m_params.size)
    vec_free_val = generate_random_vec_free_val(m_params.size)
    return InputData(m_params, matrix, vec_free_val)


def read_from_file(path: str):
    """
    File format:
        size
        accuracy
        1.0 1.0 - matrix A
        2.0 3.0 - matrix A
        1.0 2.0 - vector b
    """
    with open(path, "r") as f:
        size: int = int(f.readline())
        accuracy = float(f.readline())
        matrix = np.loadtxt(f, delimiter=" ", dtype=np.double, max_rows=size)
        if matrix.shape[0] != size or matrix.shape[1] != size:
            raise InvalidDataFormat("Размер матрицы A не соответствует введенному")
        vec_b = np.loadtxt(f, delimiter=" ", dtype=np.double, max_rows=1)
        if vec_b.shape[0] != size:
            raise InvalidDataFormat("Размер вектора b не соответствует введенному")
        return InputData(MatrixParams(size, accuracy), matrix, vec_b)


def print_indexed_vector(label: str, vector):
    print(label)
    for i, x in enumerate(vector):
        print(f"{i+1}: {x}")


def print_results(results: Results):
    print("Матрица:\n", results.matrix)
    print("Вектор b:\n", results.vec_b, "\n")

    print_indexed_vector("Корни", results.roots)
    print_indexed_vector("Погрешность", results.inaccuracy)
    print(f"Количество итераций: {results.amount_iter}\n\n")

