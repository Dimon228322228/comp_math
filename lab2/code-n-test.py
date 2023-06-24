#!/bin/python3

import math
import os
import random
import re
import sys


# x -> sin(x)
def first_function(args: []) -> float:
    return math.sin(args[0])


# (x, y) -> (x + y)/2
def second_function(args: []) -> float:
    return (args[0] * args[1]) / 2


# (x, y) -> x^2 * y^2 - 3x^3 - 6y^3 + 8
def third_function(args: []) -> float:
    return pow(args[0], 2) * pow(args[1], 2) - 3 * pow(args[0], 3) - 6 * pow(args[1], 3) + 8


# (x, y) -> x^4 - 9y + 2
def fourth_function(args: []) -> float:
    return pow(args[0], 4) - 9 * args[1] + 2


# (x, y, z) -> x + x^2 - 2yz - 0.1
def fifth_function(args: []) -> float:
    return args[0] + pow(args[0], 2) - 2 * args[1] * args[2] - 0.1


# (x, y, z) -> y + y^2 + 3xz + 0.2
def six_function(args: []) -> float:
    return args[1] + pow(args[1], 2) + 3 * args[0] * args[2] + 0.2


# (x, y, z) -> z + z^2 + 2xy - 0.3
def seven_function(args: []) -> float:
    return args[2] + pow(args[2], 2) + 2 * args[0] * args[1] - 0.3


def default_function(args: []) -> float:
    return 0.0


# How to use this function:
# funcs = Result.get_functions(4)
# funcs[0](0.01)
def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        return [third_function, fourth_function]
    elif n == 3:
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]


#
# Complete the 'solve_by_fixed_point_iterations' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER system_id
#  2. INTEGER number_of_unknowns
#  3. DOUBLE_ARRAY initial_approximations
#
# 1 - 1, 2, [0.0, 0.0]
# 2 - 3, 3, [0.0, 0.0, 0.0]
# 3 - 4, 1, [0.0]


def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    def system_equations(system, approximation):
        for i in range(len(system)):
            approximation[i] = system[i](approximation) + approximation[i]
        return approximation

    def update_solution(solution, system_id):
        if system_id == 1:
            return [math.asin(solution[0]), 0.0]
        elif system_id == 2:
            return [((3 * pow(solution[0], 3) - 8) / pow(solution[1], 2) + 6 * solution[1])**0.5, (pow(solution[0], 4) + 2) / 9]
        elif system_id == 3:
            return [
                 -pow(solution[0], 2) + 2 * solution[1] * solution[2] + 0.1,
                 -pow(solution[1], 2) - 3 * solution[0] * solution[2] - 0.2,
                 -pow(solution[2], 2) - 2 * solution[0] * solution[1] + 0.3
            ]
        else:
            return [0.0]

    system = get_functions(system_id)
    max_iterations = 300
    tolerance = 1e-8
    solution = initial_approximations
    iterations = 1
    next_solution = update_solution(solution, system_id)

    while all(abs(next_solution[i] - solution[i]) > tolerance for i in range(len(solution))) and iterations < max_iterations:
        next_solution = update_solution(solution, system_id)  # Вычисляем следующее приближение
        solution = next_solution
        iterations += 1

    return solution


if __name__ == '__main__':
    system_id = int(input().strip())

    number_of_unknowns = int(input().strip())

    initial_approximations = []

    for _ in range(number_of_unknowns):
        initial_approximations_item = float(input().strip())
        initial_approximations.append(initial_approximations_item)

    result = solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations)

    print('\n'.join(map(str, result)))