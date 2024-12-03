from .main import part1, part2


INPUT_A = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

INPUT_B = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def test_part1():
    assert part1(INPUT_A) == 161


def test_part2():
    assert part2(INPUT_B) == 48


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 178538786
    assert part2(input) == 102467299
