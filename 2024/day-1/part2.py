import helpers


def find_frequencies(data: list[int]) -> dict[int, int]:
    frequencies: dict[int, int] = {}
    for number in data:
        frequencies[number] = frequencies.get(number, 0) + 1
    return frequencies


def solve(data: list[str]) -> int:
    pairs = helpers.get_pairs(data)
    right_frequencies = find_frequencies(pairs.right)
    similarity_score = 0
    for number in pairs.left:
        similarity_score += number * right_frequencies.get(number, 0)
    return similarity_score
