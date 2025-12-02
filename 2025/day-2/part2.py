def find_repeated_digits_count(id: str) -> int:
    if len(id) < 2:
        return 0

    repeated_seq_size = (id + id).index(id, 1)
    if not repeated_seq_size < len(id):
        return 0
    return int(len(id) / repeated_seq_size)


def is_invalid_id(id: int) -> bool:
    return find_repeated_digits_count(str(id)) >= 2


def find_invalid_ids(start_id: int, end_id: int) -> list[int]:
    invalid_ids: list[int] = [
        id for id in range(start_id, end_id + 1) if is_invalid_id(id)
    ]
    return invalid_ids


def solve(data: list[str]) -> int:
    sum_of_invalid_ids = 0
    for id_range in data:
        (start_id, end_id) = id_range.split("-")
        sum_of_invalid_ids += sum(find_invalid_ids(int(start_id), int(end_id)))
    return sum_of_invalid_ids
