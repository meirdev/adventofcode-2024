from .main import part1, part2


INPUT = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


def test_part1():
    assert part1(INPUT) == 12


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 226236192
    assert part2(input) == 8168
