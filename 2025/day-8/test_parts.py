import part1
import part2

from typing import List, cast

import pytest


def test_part1():
    test_input = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
        """.strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 40
    assert part1.solve(test_input) == expected_output


@pytest.mark.skip(reason="not implemented yet")
def test_part2():
    test_input = """
        """.strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 0
    assert part2.solve(test_input) == expected_output


@pytest.mark.skip(reason="not implemented yet")
def test_complete_part1():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 0
    assert part1.solve(input_data) == expected_output


@pytest.mark.skip(reason="not implemented yet")
def test_complete_part2():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 0
    assert part2.solve(input_data) == expected_output
