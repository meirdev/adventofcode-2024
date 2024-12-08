from .main import part1, part2


INPUT = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def test_part1():
    assert part1(INPUT) == 14


def test_part2():
    assert part2(INPUT) == 34


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 379
    assert part2(input) == 1339