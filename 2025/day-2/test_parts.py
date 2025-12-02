import part1
import part2

from typing import List, cast


def test_part1():
    test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""".split(
        ","
    )
    test_input = cast(List[str], test_input)
    expected_output = 1227775554
    assert part1.solve(test_input) == expected_output


def test_part2():
    test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""".split(
        ","
    )
    test_input = cast(List[str], test_input)
    expected_output = 4174379265
    assert part2.solve(test_input) == expected_output


def test_part2_with_manual_input():
    test_input = """12341234-12341234,123123123-123123123,1212121212-1212121212,1111111-1111111""".split(
        ","
    )
    test_input = cast(List[str], test_input)
    expected_output = 1348696680
    assert part2.solve(test_input) == expected_output


def test_solve_complete_input_part1():
    with open("input.txt") as f:
        input_data = f.read().split(",")
    assert part1.solve(input_data) == 12850231731


def test_solve_complete_input_part2():
    with open("input.txt") as f:
        input_data = f.read().split(",")
    assert part2.solve(input_data) == 24774350322
