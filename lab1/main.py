import numpy as np

from TypeModule import InputData
from matrixAction import NoDiagonallyDominantException
from IOmodule import read_from_user, read_from_file, read_and_gen_random_matrix, print_results
from solve import matrix_resolve, per_element_resolve


class NoSuchMethodException(Exception):
    pass


def show_solution(in_data: InputData, use_matrix_solution: bool):
    if use_matrix_solution:
        solution = matrix_resolve(in_data.matrix,
                                  in_data.vec_free_val,
                                  np.zeros_like(in_data.vec_free_val),
                                  in_data.params.accuracy)
        print("---- Решение матричным способом -----")
    else:
        solution = per_element_resolve(in_data.matrix,
                                       in_data.vec_free_val,
                                       np.zeros_like(in_data.vec_free_val),
                                       in_data.params.accuracy)
        print("---- Поэлементное решение -----")
    print_results(solution)


def main():
    print(
        "Решение СЛАУ в виде Ax=b, где A - матрица коэффициентов, x - вектор переменных, и b - вектор значений, методом простых итераций")
    print("0 - ввод с консоли, 1 - чтение с файла, 2 - сгенерировать случайную матрицу")
    print("Выберите формат ввода данных: ")
    format: int = int(input())
    if format == 0:
        input_data = read_from_user()
    elif format == 1:
        path: str = str(input("Введите имя файла: "))
        input_data = read_from_file(path)
    elif format == 2:
        input_data = read_and_gen_random_matrix()
    else:
        raise NoSuchMethodException("Нет такого ввода данных!")
    try:
        show_solution(input_data, False)
    except NoDiagonallyDominantException as e:
        print(e)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
