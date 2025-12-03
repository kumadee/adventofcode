import part1
import part2

from typing import List, cast


def test_part1():
    test_input = """
        987654321111111
        811111111111119
        234234234234278
        818181911112111
        818181811112111
    """.strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 357 + 88
    assert part1.solve(test_input) == expected_output


def test_part2():
    test_input = """
        987654321111111
        811111111111119
        234234234234278
        818181911112111
        818181811112111
    """.strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 3121910778619 + 888811112111
    assert part2.solve(test_input) == expected_output
