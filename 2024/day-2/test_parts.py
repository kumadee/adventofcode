import part1
import part2

from typing import List, cast


def test_part1():
    test_input = """
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
    """.strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 2
    assert part1.solve(test_input) == expected_output


def test_part2():
    test_input = """
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
    """.strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 0
    assert part2.solve(test_input) == expected_output
