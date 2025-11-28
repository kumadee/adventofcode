import helpers


def solve(data: list[str]) -> int:
    distance = 0
    pairs = helpers.get_pairs(data)
    pairs.left = sorted(pairs.left)
    pairs.right = sorted(pairs.right)

    for left, right in zip(pairs.left, pairs.right):
        distance += abs(left - right)

    return distance
