from .main import part1, part2


INPUT = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def test_part1():
    assert part1(INPUT) == 41


def test_part2():
    assert part2(INPUT) == 6


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 4826
    assert part2(input) == 1721
