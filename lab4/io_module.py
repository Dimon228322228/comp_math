from data import FUNCTIONS


def print_indexed_vector(label: str, vector):
    print(label)
    for i, x in enumerate(vector):
        print(f"{i + 1}: {x}")


def read_data():
    is_correct = False
    while True:
        print("Введите набор точек в виде: ")
        print("x_0 x_1 x_2 ... x_m")
        print("y_0 y_1 y_2 ... y_m")
        print("В отдельной строчке абсциссы или ординаты разделенные пробелом.")
        x_data, y_data = [], []
        try:
            x_data = list(map(float, input().strip().split()))
            y_data = list(map(float, input().strip().split()))
            if len(x_data) == len(y_data):
                is_correct = True
            else:
                print("Количество абсцисс и ординат должно совпадать.")
        except Exception as e:
            print(e)
        if is_correct:
            return x_data, y_data


def read_degree():
    while True:
        print("Введите целую степень m аппроксимирующего полинома"
              "(P(x) = a_0 + a_1*f(x) + a_2 * (f(x))^2 + ... + a_m * (f(x))^m): ")
        try:
            degree: int = int(input())
            return degree
        except Exception as e:
            print(e)


def show_function():
    for i in range(len(FUNCTIONS)):
        print(f"Номер {i + 1}: {FUNCTIONS[i].description}")


def choose_function():
    while True:
        print("Введите номер f(x) аппроксимирующего полинома"
              "(P(x) = a_0 + a_1*f(x) + a_2 * (f(x))^2 + ... + a_m * (f(x))^m): ")
        show_function()
        try:
            num: int = int(input())
            if (num > len(FUNCTIONS)):
                print(f"Неверный номер функции")
                continue
            return num - 1
        except Exception as e:
            print(e)


def read_format_input():
    while True:
        try:
            format_input: int = int(
                input("Введите способ ввода исходных данных: 1 - автогенерация по функции или 2 - ввод вручную: "))
        except Exception as e:
            print(e)
            continue
        if format_input == 1 or format_input == 2:
            return format_input
        else:
            print("Невозможный способ ввода")


def read_boundaries():
    while True:
        try:
            a, b = list(map(int, input("Введите границы интервала [a, b]: ").strip().split()))
        except Exception as e:
            print(e)
            continue
        if a > b:
            return b, a
        return a, b
