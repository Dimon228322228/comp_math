#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'approximate_linear_least_squares' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. DOUBLE_ARRAY x_axis
#  2. DOUBLE_ARRAY y_axis
#

def approximate_linear_least_squares(x_axis, y_axis):
    n = len(x_axis)

    sum_x = sum(x_axis)
    sum_y = sum(y_axis)
    sum_x2 = sum(x ** 2 for x in x_axis)
    sum_xy = sum(x * y for x, y in zip(x_axis, y_axis))

    denominator = n * sum_x2 - sum_x ** 2
    m = (n * sum_xy - sum_x * sum_y) / denominator
    c = (sum_y * sum_x2 - sum_x * sum_xy) / denominator

    y_fit = [m * x + c for x in x_axis]
    y_deviation = [(y - f_x)**2 for y, f_x in zip(y_axis, y_fit)]

    return max(y_deviation)


if __name__ == '__main__':
    axis_count = int(input().strip())

    x_axis = list(map(float, input().rstrip().split()))

    y_axis = list(map(float, input().rstrip().split()))

    result = approximate_linear_least_squares(x_axis, y_axis)

    print(str(result) + '\n')
