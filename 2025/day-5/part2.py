from dataclasses import dataclass


@dataclass
class IdRange:
    start_id: int
    end_id: int

    def is_id_in(self, id: int):
        return self.start_id <= id <= self.end_id


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
    fresh_ingredient_ids = set()
    # print(f"fresh_ingredients_ranges: {fresh_ingredients_ranges}")
    for _range in fresh_ingredients_ranges:
        for id in range(_range.start_id, _range.end_id + 1):
            fresh_ingredient_ids.add(id)

    return len(fresh_ingredient_ids)
