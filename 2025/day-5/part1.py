from dataclasses import dataclass


@dataclass
class IdRange:
    start_id: int
    end_id: int

    def is_id_in(self, id: int):
        return self.start_id <= id <= self.end_id


def ingredient_id_in_range(id: int, fresh_ingredients_ranges: list[IdRange]) -> bool:
    for id_range in fresh_ingredients_ranges:
        if id_range.is_id_in(id):
            # print(f"id: {id} is in range {id_range.start_id}-{id_range.end_id}")
            return True
    return False


def newRange(id: str) -> IdRange:
    _range = id.split("-")
    if len(_range) != 2:
        raise ValueError(f"Invalid range {id}, splitting doesn't result in 2 items")
    start = int(_range[0])
    end = int(_range[1])
    if start > end:
        raise ValueError(f"Invalid range {id}, start is greater than end")
    return IdRange(start_id=start, end_id=end)


def solve(data: list[str]) -> int:
    blank_line_index = 0
    for i, line in enumerate(data):
        if len(line.strip()) == 0:
            blank_line_index = i
            break
    fresh_ingredients_ranges = [
        newRange(id_range) for id_range in data[0:blank_line_index]
    ]
    available_ingredients: list[int] = [int(id) for id in data[blank_line_index + 1 :]]
    # print(f"fresh_ingredients_ranges: {fresh_ingredients_ranges}")
    # print(f"available_ingredients: {available_ingredients}")

    tmp = [
        1
        for id in available_ingredients
        if ingredient_id_in_range(id, fresh_ingredients_ranges)
    ]
    # print(f"tmp: {tmp}")
    fresh_ingredients_count = sum(tmp)
    return fresh_ingredients_count
