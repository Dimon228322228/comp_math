from custom_types import Equation, Fun
from methods import simple_iterations_method_for_system, simple_iterations_method, bisection_method
from util.results_output import print_results
from util.tests import TEST_SYSTEM, TEST_FUNCTIONS, SYSTEM


def show_system():
    for i, x in enumerate(SYSTEM):
        print(f"Номер {i}")
        for j in range(len(x)):
            print(f" ---   {x[j].description}   ---")

def show_func():
    for i in range(len(TEST_FUNCTIONS)):
        print(f" ---  {i} {TEST_FUNCTIONS[i].description}   ---")


def show_nonlinear_system_solution(number, initial_approc):
    print("Решение системы нелинейных уравнений...")
    for i in range(len(SYSTEM[number])):
        print(f" ---   {SYSTEM[number][i].description}   ---")
    try:
        result = simple_iterations_method_for_system(system=SYSTEM[number],
                                                     initial_approximations=initial_approc)
        print("Результат с помощью метода простых итераций: ")
        print_results(result)
    except Exception as e:
        print("Невозможно вычислить")


def solve_equation(num, initial_approc, a, b):
    function: Fun = TEST_FUNCTIONS[num]
    try:
        bisection_result = bisection_method(function.f_x, a=a, b=b)
    except Exception as e:
        print("Невозможно вычислить")
        return
    try:
        iterations_result = simple_iterations_method(function.g_x_for_iter, a=a, b=b, approximation=initial_approc[0])
    except Exception as e:
        print("Невозможно вычислить")
        return
    print(f"---{function.description}---")
    print(
        f"Результат метода деления пополам: {bisection_result.root}; количество итераций: {bisection_result.iterations}")
    print(
        f"Результат метода простых итераций: {iterations_result.root}; количество итераций: {iterations_result.iterations}")
    print(f"Разница между решениями: {abs(iterations_result.root - bisection_result.root)}\n\n")


def main():
    print("Решение СНАУ методом простых итераций и решение нелинейных уравнений методами деления пополам и простых итераций")
    format: int = int(input("Введите число, 0 - решаем систему, а 1 - просто уравнения: "))
    if format == 0:
        show_system()
    elif format == 1:
        show_func()
    else:
        print("Неверный ввод")
        return
    which: int = int(input(" Введите номер системы или уравнения: "))
    initial_approximation = list(map(float, str(input("Введите начальные условия: ")).strip().split(" ")))
    if format == 0:
        show_nonlinear_system_solution(which, initial_approximation)
    elif format == 1:
        a, b = map(float, str(input("Введите концы отрезка: ")).strip().split(" "))
        solve_equation(which, initial_approximation, a, b)


if __name__ == "__main__":
    main()
