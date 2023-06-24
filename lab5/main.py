from custom_type import Equation_with_3_arg
from data import FUNCTIONS
from io_module import choose_function, read_float
from least_square_method.least_square_method import least_square_solve
from runge_kutta_method import solve_by_runge_kutta
import matplotlib.pyplot as plt


def generate_by_function(func: Equation_with_3_arg, a, y_a, b):
    x, y = [], []
    c = a
    while c < b:
        x.append(c)
        y.append(func(c, y_a, a))
        c += 0.001
    return x, y


def main():
    num_f = choose_function()
    epsilon = read_float("Введите точность ")
    a = read_float("Введите абсциссу начальной точки ")
    y_a = read_float("Введите ординату начальной точки ")
    b = read_float("Введите абсциссу конечной точки ")

    x_data, y_data = solve_by_runge_kutta(num_f=num_f, epsilon=epsilon, a=a, b=b, y_a=y_a)
    result = least_square_solve(x_data=x_data, y_data=y_data, max_degree=1, func=FUNCTIONS[num_f].analitic_solve_func, a=a, y_a=y_a)
    if not result.is_calculate:
        print("Невозможно сделать интерполяцию: проверьте область определения функций, иначе невозможно разрешить СЛАУ")
        return

    def approximate_func(x, y_a, a):
        s = 0
        for i in range(2):
            s += result.coefficients[i] * FUNCTIONS[num_f].analitic_solve_func(x, y_a, a) ** i
        return s

    x, y = generate_by_function(FUNCTIONS[num_f].analitic_solve_func, a, y_a, b)
    x_fit, y_fit = generate_by_function(approximate_func, a, y_a, b)
    fig, ax = plt.subplots()

    ax.plot(x, y, color='yellow', label=f"Аналитическое решение")
    ax.scatter(x_fit, y_fit, color='green', label=f"Численное решение", linewidths=0.1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Графики функций')

    ax.legend()
    plt.show()


if __name__ == '__main__':
    main()
