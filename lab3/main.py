from data import getAllFun
from simpsons_method import calculate_integral


def show_functions():
    for index, function in enumerate(getAllFun()):
        print(f"Номер {index + 1}:")
        print(f"{function.description}\n")


if __name__ == '__main__':
    show_functions()
    f = int(input("Введите номер функции: ").strip())
    a = float(input("Введите нижнюю границу интервала: ").strip())
    b = float(input("Введите верхнюю границу интервала: ").strip())
    epsilon = float(input("Введите желаемую точность расчета: ").strip())

    result = calculate_integral(a, b, f, epsilon)
    if result.has_solve:
        print(f"Результат: {str(result.sum)}, полученный при разбиении отрезка на {result.partition} частей")
    else:
        print(f"{result.err}")
