from .main import part1, part2


INPUT = "125 17"


def test_part1():
    assert part1(INPUT) == 55312


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 188902
    assert part2(input) == 223894720281135
