#!/bin/python3

import math
import os
import random
import re
import sys


class Result:
    error_message = "Integrated function has discontinuity or does not defined in current interval"
    has_discontinuity = False
    eps = 0.000001

    def first_function(x: float):
        return 1 / x

    def second_function(x: float):
        if x == 0:
            return (math.sin(Result.eps) / Result.eps + math.sin(-Result.eps) / -Result.eps) / 2
        return math.sin(x) / x

    def third_function(x: float):
        return x * x + 2

    def fourth_function(x: float):
        return 2 * x + 2

    def five_function(x: float):
        return math.log(x)

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
        elif n == 5:
            return Result.five_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")

    #
    # Complete the 'calculate_integral' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. DOUBLE a
    #  2. DOUBLE b
    #  3. INTEGER f
    #  4. DOUBLE epsilon
    #

    def calculate_integral(a, b, f, epsilon):
        func = Result.get_function(f)
        is_reverse: bool = a > b

        def is_invalid(val):
            return math.isnan(func(val)) or math.isinf(func(val))

        if is_reverse:
            a, b = b, a
        dx = 0.0000001
        n = 100
        old_sum = 0
        while True:
            sum = 0
            h = (b - a) / n

            for i in range(1, n):
                x = a + i * h
                if i % 2 == 0:
                    try:
                        if is_invalid(x) and not is_invalid(x + dx) and not is_invalid(x - dx):
                            sum += func(x + dx) + func(x - dx)
                        elif is_invalid(x):
                            Result.has_discontinuity = True
                            return
                        else:
                            sum += 2 * func(x)
                    except Exception as e:
                        Result.has_discontinuity = True
                        return
                else:
                    try:
                        if is_invalid(x) and not is_invalid(x + dx) and not is_invalid(x - dx):
                            sum += 2 * (func(x + dx) + func(x - dx))
                        elif is_invalid(x):
                            Result.has_discontinuity = True
                            return
                        else:
                            sum += 4 * func(x)
                    except Exception as e:
                        Result.has_discontinuity = True
                        return

            def calc_boundary(k):
                if is_invalid(k) and not is_invalid(k + dx) and not is_invalid(k - dx):
                    return (func(k + dx) + func(k - dx)) / 2
                elif is_invalid(k):
                    return math.nan
                else:
                    return func(k)

            try:
                f_a = calc_boundary(a)
                f_b = calc_boundary(b)
                if math.isnan(f_a) or math.isnan(f_b):
                    Result.has_discontinuity = True
                    return
                sum += f_a + f_b
            except Exception as e:
                Result.has_discontinuity = True
                return
            sum = h / 3 * sum
            if abs(sum - old_sum) > epsilon:
                old_sum = sum
                n *= 2
                continue
            if is_reverse:
                return -sum
            else:
                return sum


if __name__ == '__main__':

    a = float(input().strip())

    b = float(input().strip())

    f = int(input().strip())

    epsilon = float(input().strip())

    result = Result.calculate_integral(a, b, f, epsilon)
    if not Result.has_discontinuity:
        print(str(result) + '\n')
    else:
        print(Result.error_message + '\n')
