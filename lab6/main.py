from lab6.data import FUNCTIONS
from lab6.io_module import IO
from lab6.chebyshev_scaler import ChebyshevInterpolation
from lab6.lagrange_interpol import LagrangeInterpolation
from lab6.graph import Graph
import numpy as np


def create_noise(y):
    c = min(y) * 0.05
    noise = np.random.uniform(-c, c, len(y))
    return noise


def main():
    io_module = IO()
    io_module.print_list([i.descr for i in FUNCTIONS], "Выберите номер функции для интерполяции")
    num_f = io_module.read_num_f(1, len(FUNCTIONS)) - 1
    f = FUNCTIONS[num_f].f
    a, b = io_module.read_boundaries()
    n = io_module.read_dot_amount()
    cholesky = ChebyshevInterpolation(a, b)
    x_unit_cholesky = cholesky.get_root_by_section(n)
    y_unit_cholesky = [f(x) for x in x_unit_cholesky]
    noise = create_noise(y_unit_cholesky)
    y_unit_cholesky += noise
    x_unit_linear = []
    x = a
    step = (b - a) / n
    for i in range(len(y_unit_cholesky)):
        x_unit_linear.append(x)
        x += step
    y_unit_linear = [f(x) for x in x_unit_linear]
    y_unit_linear += noise
    lagrange_cholesky = LagrangeInterpolation(x_unit_cholesky, y_unit_cholesky)
    lagrange_linear = LagrangeInterpolation(x_unit_linear, y_unit_linear)
    x_data, y_real, y_approximate_cholesky, y_approximate_linear = [], [], [], []
    x = a
    step = 0.001 if 0.001 < 1 / n else 1 / (2 * n)
    while x < b:
        x_data.append(x)
        y_real.append(f(x))
        y_approximate_cholesky.append(lagrange_cholesky.calc_lagrange_by_point(x))
        y_approximate_linear.append(lagrange_linear.calc_lagrange_by_point(x))
        x += step
    graph = Graph()
    graph.set_graph_title("Интерполяция и реальная функция") \
        .set_x_axis("X") \
        .set_y_axis("Y") \
        .add_blue_plot(x_data, y_real, "Исходная функция") \
        .add_red_plot(x_data, y_approximate_cholesky, "Интерполяция с x_i Чебышева")
    # graph.add_green_plot(x_data, y_approximate_linear, "Интерполяция с линейным x_i")
    graph.add_init_black_data(x_unit_cholesky, y_unit_cholesky).show()
    err = max([abs(y_r - y_a) for y_r, y_a in zip(y_real, y_approximate_cholesky)])
    print(err)


if __name__ == "__main__":
    main()
