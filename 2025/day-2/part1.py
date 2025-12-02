import math


def split_id_in_half(id: int, digits_count: int) -> tuple[int, int]:
    return divmod(id, 10 ** math.floor(digits_count / 2))


def find_num_of_digits(id: int) -> int:
    return math.floor(math.log(id, 10)) + 1


def is_invalid_id(id: int) -> bool:
    digit_count = find_num_of_digits(id)
    if digit_count % 2 != 0:
        # can't split in half
        return False
    (first_half, second_half) = split_id_in_half(id, digit_count)
    # print(f"id: {id}, first_half: {first_half}, second_half: {second_half}")
    return first_half == second_half


def find_invalid_ids(start_id: int, end_id: int) -> list[int]:
    invalid_ids: list[int] = [
        id for id in range(start_id, end_id + 1) if is_invalid_id(id)
    ]
    # print(f"start_id: {start_id}, end_id: {end_id}, invalid_ids: {invalid_ids}")
    return invalid_ids


def solve(data: list[str]) -> int:
    sum_of_invalid_ids = 0
    for id_range in data:
        (start_id, end_id) = id_range.split("-")
        sum_of_invalid_ids += sum(find_invalid_ids(int(start_id), int(end_id)))
    return sum_of_invalid_ids
