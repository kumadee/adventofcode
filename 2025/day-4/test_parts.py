import part1
import part2

from typing import List, cast

import pytest


def test_part1():
    test_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 13
    assert part1.solve(test_input) == expected_output


def test_part1_with_example():
    test_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
..........
.@.@.@.@.@
..........""".splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 13 + 5
    assert part1.solve(test_input) == expected_output


def test_part2():
    test_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 43
    assert part2.solve(test_input) == expected_output


def test_complete_part1():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 1370
    assert part1.solve(input_data) == expected_output


def test_complete_part2():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 8437
    assert part2.solve(input_data) == expected_output
