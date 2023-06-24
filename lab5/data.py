import math

from custom_type import Fun


def third_analitic_function(x: int, y_a: float, a: float):
    if y_a ** 2 - 2 * a - 1 < 0:
        raise ValueError("Invalid prerequisite")
    c = math.sqrt(y_a ** 2 - 2 * a - 1) / math.e ** a
    return math.sqrt((c * math.e ** x) ** 2 + 2 * x + 1)


FUNCTIONS = [
    Fun(description="f'(x) = sin(x)",
        f=lambda x, y: math.sin(x),
        short_description="sin(x)",
        analitic_solve_func=lambda x, y_a, a: y_a + math.cos(a) - math.cos(x)),
    Fun(description="f'(x) = x * y / 2",
        f=lambda x, y: x * y / 2,
        short_description="x * y / 2",
        analitic_solve_func=lambda x, y_a, a: y_a / (math.e ** (a**2 / 4)) * math.e ** (x**2 / 4)),
    Fun(description="f'(x) = y - (2 * x) / y",
        f=lambda x, y: y - (2 * x) / y,
        short_description="y - (2 * x) / y",
        analitic_solve_func=lambda x, y_a, a: third_analitic_function(x, y_a, a)),
    Fun(description="f'(x) = x + y",
        f=lambda x, y: x + y,
        short_description="x + y",
        analitic_solve_func=lambda x, y_a, a: (y_a + a + 1) / (math.e ** a) * math.e ** x - x - 1),
]
