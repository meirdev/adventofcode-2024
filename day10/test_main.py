import pytest

from .main import part1, part2


INPUT_1 = """
0123
1234
8765
9876
"""

INPUT_2 = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


@pytest.mark.parametrize("test_input,expected", [(INPUT_1, 1), (INPUT_2, 36)])
def test_part1(test_input, expected):
    assert part1(test_input) == expected


def test_part2():
    assert part2(INPUT_2) == 81


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 733
    assert part2(input) == 1514
