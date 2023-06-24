from custom_type import x_data, y_data
from data import FUNCTIONS


def solve_by_runge_kutta(num_f, epsilon, a, y_a, b) -> tuple[x_data, y_data]:
    f = FUNCTIONS[num_f].f
    analitic_fun = FUNCTIONS[num_f].analitic_solve_func
    x_data, y_data = [], []
    x_data.append(a)
    y_data.append(y_a)
    h = 0.01
    while True:
        n = int((b - a) / h)
        for i in range(n):
            k_1 = h * f(x_data[len(x_data) - 1], y_data[len(y_data) - 1])
            k_2 = h * f(x_data[len(x_data) - 1] + h / 2, y_data[len(y_data) - 1] + k_1 / 2)
            k_3 = h * f(x_data[len(x_data) - 1] + h / 2, y_data[len(y_data) - 1] + k_2 / 2)
            k_4 = h * f(x_data[len(x_data) - 1] + h, y_data[len(y_data) - 1] + k_3)
            y_data.append(y_data[len(y_data) - 1] + (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6)
            x_data.append(x_data[len(x_data) - 1] + h)
        if (y_data[len(y_data) - 1] - analitic_fun(b, y_a, a)) > epsilon:
            h /= 2
        else:
            return x_data, y_data
