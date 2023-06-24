import math
from typing import List

from custom_types import Fun


def second_function(x: float):
    if x == 0:
        return (math.sin(0.0001) / 0.0001 + math.sin(-0.0001) / -0.0001) / 2
    return math.sin(x) / x


__FUNCTIONS: List[Fun] = [
    Fun("f(x) = 1 / x ", lambda x: 1 / x),
    Fun("         /   sin(x)                                     \n"
        "        /    ------  , x != 0                           \n"
        "       /       x                                        \n"
        "f(x) =|                                                 \n"
        "       \       sin(a)  sin(-a)    1                     \n"
        "        \    ( ----- + ------ ) * - , a = 0.0001 x = 0  \n"
        "         \       a       -a       2                     ", second_function),
    Fun("f(x) =  x^2 + 2 ", lambda x: x ** 2 + 2),
    Fun("f(x) =  2x + 2 ", lambda x: 2 * x + 2),
    Fun("f(x) =  ln(x) ", lambda x: math.log(x)),
    Fun("        x^2 - 25  \n"
        "f(x) =  --------  \n"
        "         x + 5    ", lambda x: (x ** 2 - 25) / (x + 5))
]


def getFun(n: int) -> Fun:
    if n <= len(__FUNCTIONS):
        return __FUNCTIONS[n - 1]
    else:
        raise ValueError(f"Функции с номером {n} не существует!")


def getAllFun() -> List[Fun]:
    return __FUNCTIONS
