import collections
import itertools
from typing import Counter, NamedTuple, TypeAlias


Position: TypeAlias = tuple[int, int]


class Map(NamedTuple):
    guard: Position
    obstructions: list[Position]
    size: tuple[int, int]


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_input(input: str) -> Map:
    guard = (-1, -1)
    obstructions = []

    lines = input.strip().splitlines()

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                obstructions.append((y, x))
            elif char == "^":
                guard = (y, x)

    return Map(guard, obstructions, (len(lines), len(lines[0])))


def get_visited(
    guard: Position, obstructions: list[Position], map_size: tuple[int, int]
) -> list[Position] | None:
    visited: Counter[Position] = collections.Counter()

    directions = itertools.cycle(DIRECTIONS)

    direction = next(directions)

    while visited[guard] <= 4:
        visited[guard] += 1

        for _ in range(4):
            y, x = guard[0] + direction[0], guard[1] + direction[1]

            if (y, x) in obstructions:
                direction = next(directions)
                continue

            if y < 0 or y >= map_size[0] or x < 0 or x >= map_size[1]:
                return list(visited.keys())

            guard = (y, x)

            break

    return None


def part1(input: str) -> int:
    map = parse_input(input)

    visited = get_visited(map.guard, map.obstructions, map.size)

    return -1 if visited is None else len(visited)


def part2(input: str) -> int:
    map = parse_input(input)

    visited = get_visited(map.guard, map.obstructions, map.size)

    if visited is None:
        return -1

    return sum(
        get_visited(map.guard, map.obstructions + [i], map.size) is None
        for i in visited
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
