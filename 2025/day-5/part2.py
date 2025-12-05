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
    fresh_ingredients_range_dict = {}
    for _range in fresh_ingredients_ranges:
        if _range.start_id in fresh_ingredients_range_dict:
            r = fresh_ingredients_range_dict[_range.start_id]
            if _range.end_id <= r.end_id:
                continue
            r.end_id = _range.end_id
        fresh_ingredients_range_dict[_range.start_id] = _range

    fresh_ingredients_start_sorted = sorted(fresh_ingredients_range_dict.keys())
    prev_range = None
    fresh_ingredients_count = 0
    for start_id in fresh_ingredients_start_sorted:
        curr_range = fresh_ingredients_range_dict[start_id]
        if prev_range is None:
            prev_range = curr_range
            fresh_ingredients_count = curr_range.end_id - curr_range.start_id + 1
            continue
        if curr_range.start_id <= prev_range.end_id:
            curr_range.start_id = prev_range.end_id + 1

        if curr_range.start_id > curr_range.end_id:
            continue
        fresh_ingredients_count += curr_range.end_id - curr_range.start_id + 1
        prev_range = curr_range

    # print(f"fresh_ingredients_ranges: {fresh_ingredients_ranges}")
    return fresh_ingredients_count
