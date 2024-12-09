from .main import part1, part2


INPUT = """2333133121414131402"""


def test_part1():
    assert part1(INPUT) == 1928


def test_part2():
    assert part2(INPUT) == 2858


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 6262891638328
    assert part2(input) == 6287317016845
