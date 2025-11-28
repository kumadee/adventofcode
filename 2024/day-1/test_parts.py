import part1
import part2

from typing import List, cast


def test_part1():
    test_input = """
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3""".strip().splitlines()
    test_input = cast(List[str], test_input)

    expected_output = 11
    assert part1.solve(test_input) == expected_output


def test_part2():
    test_input = """
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3""".strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 31
    assert part2.solve(test_input) == expected_output
