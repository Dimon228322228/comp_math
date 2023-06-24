import math

import matplotlib.pyplot as plt
import numpy as np

from custom_type import Equation
from data import FUNCTIONS
from io_module import read_data, read_degree, choose_function, read_format_input, read_boundaries, print_indexed_vector
from least_square_method import least_square_solve

NOISE_SCALE = 0.5


def apply_noise(y):
    noise = np.random.normal(0, NOISE_SCALE, len(y))
    return y + noise


def generate_by_function(func: Equation, max_degree, a=1, b=100):
    if b - a < max_degree:
        b = a + max_degree + 10
    x = [i for i in range(a, b)]
    y = [func(x_i) for x_i in x]
    y = apply_noise(y)
    return x, y


def main():
    degree = read_degree()
    num_f = choose_function()
    format_input = read_format_input()
    real_funct_str = ""
    for i in range(degree + 1):
        if i == 0:
            real_funct_str += f"1 +"
            continue
        if i == degree:
            real_funct_str += f" {FUNCTIONS[num_f].short_description}^{i}"
            continue
        real_funct_str += f" {FUNCTIONS[num_f].short_description}^{i} +"

    def real_func(x):
        s = 0
        for i in range(degree + 1):
            s += FUNCTIONS[num_f].f(x) ** i
        return s

    if format_input == 2:
        x_data, y_data = read_data()
    elif format_input == 1:
        a, b = read_boundaries()
        x_data, y_data = generate_by_function(func=real_func, a=a, b=b, max_degree=degree)
    result = least_square_solve(x_data=x_data, y_data=y_data, max_degree=degree, func=FUNCTIONS[num_f].f)
    if not result.is_calculate:
        print("Невозможно сделать интерполяцию: проверьте область определения функций, иначе невозможно разрешить СЛАУ")
        return

    def approximate_func(x):
        s = 0
        for i in range(degree + 1):
            s += result.coefficients[i] * FUNCTIONS[num_f].f(x) ** i
        return s

    def round_to_significant(number, digits):
        if number == 0:
            return 0
        return round(number, -int(math.floor(math.log10(abs(number)))) + (digits - 1))

    str_func = ""
    for i in range(degree + 1):
        if result.coefficients[i] == 0:
            continue
        if i == 0:
            str_func += f"{round_to_significant(result.coefficients[i], 1)} +"
            continue
        if i == degree:
            str_func += f" {round_to_significant(result.coefficients[i], 1)}*{FUNCTIONS[num_f].short_description}^{i}"
            continue
        str_func += f" {round_to_significant(result.coefficients[i], 1)}*{FUNCTIONS[num_f].short_description}^{i} +"

    x_appox_data = np.linspace(min(x_data), max(x_data), 500)
    y_approx_data = [approximate_func(x) for x in x_appox_data]

    x_real_data = np.linspace(min(x_data), max(x_data), 500)
    y_real_data = [real_func(x) for x in x_appox_data]

    y_deviation = [(y - f_x) ** 2 for y, f_x in zip(y_real_data, y_approx_data)]
    print(f"Максимальный квадрат отклонения: {max(y_deviation)}")

    fig, ax = plt.subplots()

    ax.plot(x_appox_data, y_approx_data, color='blue', label=f"{str_func}")
    ax.plot(x_real_data, y_real_data, color='green', label=f"{real_funct_str}")
    ax.scatter(x_data, y_data, edgecolors='black', label="Исходные данные")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Рисунок {real_funct_str} и аппроксимации')

    ax.legend()
    plt.show()


if __name__ == '__main__':
    main()
