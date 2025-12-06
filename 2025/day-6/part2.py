from functools import reduce


def do_math(numbers_matrix: list[list[int]], operations: list[str]) -> int:
    if len(numbers_matrix) != len(operations):
        raise ValueError(
            f"Length of numbers_matrix: {len(numbers_matrix)} is not same as operators length: {len(operations)}"
        )
    result = 0
    for i, op in enumerate(operations):
        numbers: list[int] = numbers_matrix[i]
        if op == "+":
            result += sum(numbers)
        elif op == "*":
            result += reduce(lambda x, y: x * y, numbers)
        else:
            raise ValueError(f"Unknown operation {op}")

    return result


def read_cephalopod_numbers(cepha_nums: list[str]) -> list[list[int]]:
    numbers_matrix: list[list[int]] = []
    numbers = []
    for i in range(len(cepha_nums[0])):
        number = "".join([line[i] for line in cepha_nums]).strip()
        if number != "":
            numbers.append(int(number))
        if number == "" or i == len(cepha_nums[0]) - 1:
            numbers_matrix.append(numbers)
            numbers = []
            continue
    # print(f"numbers_matrix: {numbers_matrix}")
    return numbers_matrix


def solve(data: list[str]) -> int:
    numbers_matrix = read_cephalopod_numbers(data[0 : len(data) - 1])
    operations: list[str] = data[len(data) - 1].split()
    return do_math(numbers_matrix, operations)
