from data import FUNCTIONS


def show_function():
    for i in range(len(FUNCTIONS)):
        print(f"Номер {i + 1}: {FUNCTIONS[i].description}")


def choose_function():
    while True:
        print("Введите номер уравнения")
        show_function()
        try:
            num: int = int(input())
            if (num > len(FUNCTIONS)):
                print(f"Неверный номер")
                continue
            return num - 1
        except Exception as e:
            print(e)


def read_float(label: str):
    while True:
        try:
            return float(input(label).strip())
        except Exception as e:
            print(e)
