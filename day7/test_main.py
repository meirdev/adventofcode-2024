from .main import part1, part2


INPUT = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def test_part1():
    assert part1(INPUT) == 3749


def test_part2():
    assert part2(INPUT) == 11387


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 932137732557
    assert part2(input) == 661823605105500
