import part1
import part2

from typing import List, cast


def test_part1():
    test_input = """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82""".strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 3
    assert part1.solve(test_input) == expected_output


def test_part2():
    test_input = """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
        L184""".strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 8
    assert part2.solve(test_input) == expected_output
