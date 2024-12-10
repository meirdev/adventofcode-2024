import functools
import itertools

import networkx as nx  # type: ignore


def parse_input(input: str) -> list[list[int]]:
    return [list(map(int, line)) for line in input.strip().splitlines()]


@functools.cache
def solution(input: str) -> list[tuple[tuple[int, int], ...]]:
    topographic_map = parse_input(input)

    zeros = []
    nines = []

    G = nx.DiGraph()

    for y in range(len(topographic_map)):
        for x in range(len(topographic_map[y])):
            if topographic_map[y][x] == 0:
                zeros.append((y, x))
            elif topographic_map[y][x] == 9:
                nines.append((y, x))

            for yi, xi in ((y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)):
                try:
                    if topographic_map[yi][xi] != topographic_map[y][x] + 1:
                        raise ValueError

                    G.add_edge((y, x), (yi, xi))
                except (IndexError, ValueError):
                    pass

    return [
        tuple(nx.all_simple_paths(G, zero, nine))
        for zero, nine in itertools.product(zeros, nines)
    ]


def part1(input: str) -> int:
    return sum(len(i) > 0 for i in solution(input))


def part2(input: str) -> int:
    return sum(len(set(map(tuple, i))) for i in solution(input))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
