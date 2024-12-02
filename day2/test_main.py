from .main import part1, part2


INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def test_part1():
    assert part1(INPUT) == 2


def test_part2():
    assert part2(INPUT) == 4


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 510
    assert part2(input) == 553
