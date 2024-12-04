from .main import part1, part2


INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def test_part1():
    assert part1(INPUT) == 18


def test_part2():
    assert part2(INPUT) == 9


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 2370
    assert part2(input) == 1908
