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


def test_part2_with_example1():
    test_input = """
        9454527354735656537472876857246747554763445832354347645346455852255465346827664554778667358636366668
    """.strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 9888_8888_6668
    assert part2.solve(test_input) == expected_output


def test_part2_with_example2():
    test_input = """
        5966546654588755548354591946657465889859765969657756889447669666979883895847755487857956955568577855
    """.strip().splitlines()
    test_input = cast(List[str], test_input)
    expected_output = 9999_9999_9999
    assert part2.solve(test_input) == expected_output


def test_complete_part1():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 17263
    assert part1.solve(input_data) == expected_output
    assert part2.solve(input_data, battery_size=2) == expected_output


def test_complete_part1_solve_with_part2_solution():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 17263
    assert part2.solve(input_data, battery_size=2) == expected_output


def test_complete_part2():
    with open("input.txt") as f:
        input_data = f.readlines()
    expected_output = 170731717900423
    assert part2.solve(input_data) == expected_output
