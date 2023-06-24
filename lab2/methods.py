from typing import List

from custom_types import Equation, EquationSolution, Fun, SystemSolution


class BoundaryWrongException(Exception):
    pass


def bisection_method(f: Equation, a: float, b: float, eps: float = 1e-9, max_iteration=1000) -> EquationSolution:
    if f(a) * f(b) > 0:
        raise ValueError("Метод деления пополам неприменим, одинаковые знаки на концах отрезка")
    if f(a) == 0:
        return EquationSolution(root=a, iterations=0)
    if f(b) == 0:
        return EquationSolution(root=b, iterations=0)
    left_boundary = a
    right_boundary = b
    iterations = 0

    while abs(right_boundary - left_boundary) > eps and iterations < max_iteration:
        iterations += 1
        mid = (right_boundary + left_boundary) / 2
        if f(mid) == 0:
            return EquationSolution(root=mid, iterations=iterations)
        if f(left_boundary) * f(mid) < 0:
            right_boundary = mid
        else:
            left_boundary = mid

    return EquationSolution(root=(left_boundary + right_boundary) / 2, iterations= iterations)


def simple_iterations_method(f: Equation, a: float, b: float, approximation: float, eps: float = 1e-6,
                             max_iteration=500) -> EquationSolution:
    iterations = 1
    x_prev: float = approximation
    x: float = f(x_prev)
    while abs(x - x_prev) > eps:
        x_prev = x
        x = f(x_prev)
        iterations += 1
        if a > x or x > b:
            raise BoundaryWrongException("Выход за границы диапазона")
        if iterations > max_iteration:
            raise BoundaryWrongException("Превышено количество итераций")

    return EquationSolution(root=x, iterations=iterations)


def simple_iterations_method_for_system(system: List[Fun], initial_approximations, tolerance=1e-6, max_iterations=300):
    def update_solution(approximation):
        new_approximation = approximation.copy()
        for i in range(len(system)):
            new_approximation[i] = system[i].g_x_for_iter(*new_approximation)
        return new_approximation

    solution = initial_approximations
    iterations = 1
    next_solution = update_solution(solution)

    while all(abs(next_solution[i] - solution[i]) > tolerance for i in range(len(solution))) and iterations < max_iterations:
        next_solution = update_solution(solution)
        solution = next_solution
        iterations += 1

    return SystemSolution(roots=solution, iterations=iterations)
