#!/bin/python3

import math
import os
import random
import re
import sys


class Result:

    def first_function(x: float, y: float):
        return math.sin(x)

    def second_function(x: float, y: float):
        return (x * y) / 2

    def third_function(x: float, y: float):
        return y - (2 * x) / y

    def fourth_function(x: float, y: float):
        return x + y

    def default_function(x: float, y: float):
        return 0.0

    def third_analitic_function(y_a: float, a: float):
        if y_a**2 - 2*a - 1 < 0:
            raise ValueError("Invalid prerequisite")
        c = math.sqrt(y_a**2 - 2*a - 1) / math.e ** a
        return lambda x: math.sqrt((c * math.e ** x) ** 2 + 2 * x + 1)
    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    def get_function(n: int):
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        else:
            return Result.default_function

    def get_analitic_function(n: int, y_a: float, a: float):
        if n == 1:
            return lambda x: y_a + math.cos(a) - math.cos(x)
        elif n == 2:
            return lambda x: y_a / (math.e ** (a**2 / 4)) * math.e ** (x**2 / 4)
        elif n == 3:
            return Result.third_analitic_function(y_a, a)
        elif n == 4:
            return lambda x: (y_a + a + 1) / (math.e ** a) * math.e ** x - x - 1
        else:
            return lambda x: y_a
    #
    # Complete the 'solveByRungeKutta' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. INTEGER f
    #  2. DOUBLE epsilon
    #  3. DOUBLE a
    #  4. DOUBLE y_a
    #  5. DOUBLE b
    #
    def solveByRungeKutta(f, epsilon, a, y_a, b):
        fun = Result.get_function(f)
        analitic_fun = Result.get_analitic_function(f, y_a, a)
        x_i = a
        y_i = y_a
        h = 0.01
        while True:
            n = int((b - a) / h)
            for i in range(n):
                k_1 = h * fun(x_i, y_i)
                k_2 = h * fun(x_i + h / 2, y_i + k_1 / 2)
                k_3 = h * fun(x_i + h / 2, y_i + k_2 / 2)
                k_4 = h * fun(x_i + h, y_i + k_3)
                y_i += (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
                x_i += h
            if (y_i - analitic_fun(b)) > epsilon:
                h /= 2
            else:
                return y_i


if __name__ == '__main__':
    f = int(input().strip())

    epsilon = float(input().strip())

    a = float(input().strip())

    y_a = float(input().strip())

    b = float(input().strip())

    result = Result.solveByRungeKutta(f, epsilon, a, y_a, b)

    print(str(result) + '\n')
