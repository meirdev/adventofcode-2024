import operator
from typing import TypeAlias

import more_itertools


Report: TypeAlias = list[int]


def parse_input(input: str) -> list[Report]:
    return [list(map(int, line.split(" "))) for line in input.strip().splitlines()]


def is_safe(report: Report) -> bool:
    cmp = operator.lt if report[0] < report[1] else operator.gt
    return all(
        cmp(a, b) and 1 <= abs(a - b) <= 3
        for a, b in more_itertools.windowed(report, 2, fillvalue=0)
    )


def part1(input: str) -> int:
    reports = parse_input(input)

    return sum(map(is_safe, reports))


def part2(input: str) -> int:
    reports = parse_input(input)

    return sum(
        any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report)))
        for report in reports
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
