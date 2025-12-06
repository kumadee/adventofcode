import part1
import part2

from typing import List, cast


def test_part1():
    test_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 4277556
    assert part1.solve(test_input) == expected_output


def test_part2():
    test_input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 3263827
    assert part2.solve(test_input) == expected_output


def test_complete_part1():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 6957525317641
    assert part1.solve(input_data) == expected_output


def test_complete_part2():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 13215665360076
    assert part2.solve(input_data) == expected_output
