from .main import part1, part2


INPUT = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


def test_part1():
    assert part1(INPUT) == 1930


def test_part2():
    assert part2(INPUT) == 1206


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1494342
    assert part2(input) == 893676
