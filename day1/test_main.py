from .main import part1, part2


INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_part1():
    assert part1(INPUT) == 11


def test_part2():
    assert part2(INPUT) == 31


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 3246517
    assert part2(input) == 29379307
