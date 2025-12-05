import part1
import part2

from typing import List, cast


def test_part1():
    test_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32""".strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 3
    assert part1.solve(test_input) == expected_output


def test_part2():
    test_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32""".strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 14
    assert part2.solve(test_input) == expected_output


def test_part2_with_example():
    test_input = """
3-5
10-14
16-20
10-15
12-18

1
5
8
11
17
32""".strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 14
    assert part2.solve(test_input) == expected_output


def test_complete_part1():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 739
    assert part1.solve(input_data) == expected_output


def test_complete_part2():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 344486348901788
    assert part2.solve(input_data) == expected_output
