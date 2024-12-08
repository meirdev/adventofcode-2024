import collections
import itertools
import operator
from typing import DefaultDict, NamedTuple


class Position(NamedTuple):
    y: int
    x: int


class Map(NamedTuple):
    antennas: DefaultDict[str, set[Position]]
    all: dict[Position, bool]


def parse_input(input: str) -> Map:
    lines = input.strip().splitlines()

    antennas: DefaultDict[str, set[Position]] = collections.defaultdict(set)

    all: dict[Position, bool] = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            is_antenna = char != "."

            if is_antenna:
                antennas[char].add(Position(y, x))

            all[Position(y, x)] = is_antenna

    return Map(antennas=antennas, all=all)


def solution(input: str, any_position: bool) -> int:
    map = parse_input(input)

    antinode: set[Position] = set()

    for antennas in map.antennas.values():
        for a, b in itertools.combinations(antennas, r=2):
            y_distance, x_distance = abs(a.y - b.y), abs(a.x - b.x)

            m = (a.y - b.y) / (a.x - b.x)

            add, sub = operator.add, operator.sub

            if m < 0:
                if a.y > b.y:
                    op = add, sub, sub, add
                else:
                    op = sub, add, add, sub
            else:
                if a.y < b.y:
                    op = sub, sub, add, add
                else:
                    op = add, add, sub, sub

            while a in map.all or b in map.all:
                a = Position(op[0](a.y, y_distance), op[1](a.x, x_distance))
                b = Position(op[2](b.y, y_distance), op[3](b.x, x_distance))

                antinode |= {a, b}

                if not any_position:
                    break

    empty = {i for i in map.all if not map.all[i]}

    if any_position:
        return sum(1 for i in antinode if i in empty) + (len(map.all) - len(empty))

    return sum(1 for i in antinode if i in map.all)


def part1(input: str) -> int:
    return solution(input, any_position=False)


def part2(input: str) -> int:
    return solution(input, any_position=True)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
