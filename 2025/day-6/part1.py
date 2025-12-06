from functools import reduce


def solve(data: list[str]) -> int:
    numbers_matrix: list[list[int]] = []
    operations: list[str] = data[len(data) - 1].split()

    for line in data[0 : len(data) - 1]:
        numbers = [int(n) for n in line.split()]
        numbers_matrix.append(numbers)

    len_rows: list[int] = [len(n) for n in numbers_matrix]
    if sum(len_rows) // len(len_rows) != len_rows[0]:
        raise ValueError(
            f"Each row in numbers_matrix doesn't have same amount of columns: {len_rows}"
        )

    result = 0
    for i, op in enumerate(operations):
        numbers: list[int] = [n[i] for n in numbers_matrix]
        if op == "+":
            result += sum(numbers)
        elif op == "*":
            result += reduce(lambda x, y: x * y, numbers)
        else:
            raise ValueError(f"Unknown operation {op}")

    return result
