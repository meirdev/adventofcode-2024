from .main import part1, part2


INPUT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def test_part1():
    assert part1(INPUT) == 143


def test_part2():
    assert part2(INPUT) == 123


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 5108
    assert part2(input) == 7380
