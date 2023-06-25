from typing import List


class IO:
    def read_int(self, label) -> int:
        while True:
            try:
                return int(input(label))
            except Exception as e:
                print(e)

    def read_float(self, label) -> float:
        while True:
            try:
                return float(input(label))
            except Exception as e:
                print(e)

    def read_dot_amount(self):
        return self.read_int("Введите количество точек, которое нужно взять для интервала: ")

    def read_num_f(self, _from: int, _to: int):
        while True:
            n = self.read_int("Введите номер функции: ")
            if _from <= n <= _to:
                return n

    def read_boundaries(self) -> (float, float):
        a = self.read_float("Введите левую границу интервала: ")
        b = self.read_float("Введите правую границу интервала: ")
        if a > b:
            return b, a
        else:
            return a, b

    def print_list(self, list: List[str], label):
        print(label)
        for index, val in enumerate(list):
            print(f"{index + 1}: {val}")