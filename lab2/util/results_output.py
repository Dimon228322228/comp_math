from custom_types import SystemSolution, Vector


def print_indexed_vector(label: str, vector: Vector):
    print(label)
    for i, x in enumerate(vector):
        print(f"{i+1}: {x}")


def print_results(solution: SystemSolution):
    print_indexed_vector("Корни :", solution.roots)
    print(f"Количество итераций: {solution.iterations}\n\n")
