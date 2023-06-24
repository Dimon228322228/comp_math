from math import sin, log, e

from custom_types import Fun

TEST_FUNCTIONS = [
    Fun(" sin(x) - x^2 = 0 одз - (-inf; inf) ", lambda x: sin(x) - x ** 2, lambda x: sin(x) ** 0.5),
    Fun(" x^3 - 2 = 0 одз - (-inf; inf) ", lambda x: x ** 3 - 2, lambda x: 2 ** 0.5),
    Fun(" ln(x) + x^2 = 0 одз - (0; inf)", lambda x: log(x) + x ** 2, lambda x: e ** (-x ** 2))
]

TEST_SYSTEM = [
    Fun("  x + x^2 - 2yz - 0.1 = 0 ", lambda x, y, z: x + x ** 2 - 2 * y * z - 0.1,
        lambda x, y, z: -x ** 2 + 2 * y * z + 0.1),
    Fun("  y + y^2 + 3xz + 0.2 = 0 ", lambda x, y, z: y + y ** 2 + 3 * x * z + 0.2,
        lambda x, y, z: -y ** 2 - 3 * x * z - 0.2),
    Fun("  z + z^2 + 2yx - 0.3 = 0 ", lambda x, y, z: z + z ** 2 + 2 * y * x - 0.3,
        lambda x, y, z: -z ** 2 - 2 * y * x + 0.3)
]


def circle_eq(x, y):
    if y > 0:
        return (1 - x ** 2) ** 0.5
    else:
        return -(1 - x ** 2) ** 0.5


TEST_SYSTEM_1 = [
    Fun("  ln(x) + 2y = -1 ", lambda x, y: log(x) + 2 * y + 1, lambda x, y: e**(-1 - 2*y)),
    Fun("  x^2 + y^2 = 1  ", lambda x, y: x ** 2 + y ** 2 - 1, circle_eq)
]

SYSTEM = [
    TEST_SYSTEM,
    TEST_SYSTEM_1
]