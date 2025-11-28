from dataclasses import dataclass


@dataclass
class Pairs:
    left: list[int]
    right: list[int]


def get_pairs(data: list[str]) -> Pairs:
    left = []
    right = []
    for line in data:
        _left, _right = line.split()
        left.append(int(_left))
        right.append(int(_right))
    return Pairs(left, right)
