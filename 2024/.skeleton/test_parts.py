import part1
import part2

from typing import List, cast


def test_part1():
    test_input = """
        """.strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = ""
    assert part1.solve(test_input) == expected_output


def test_part2():
    test_input = """
        """.strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = ""
    assert part2.solve(test_input) == expected_output
