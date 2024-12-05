import collections
import contextlib
import itertools
from typing import Counter, Iterator, NamedTuple, TypeAlias

import networkx as nx  # type: ignore


Page: TypeAlias = int


class PageOrder(NamedTuple):
    first: Page
    second: Page


def parse_input(input: str) -> tuple[list[PageOrder], list[list[Page]]]:
    section_a, section_b = input.strip().split("\n\n")

    return (
        [PageOrder(*map(int, line.split("|"))) for line in section_a.splitlines()],
        [list(map(int, line.split(","))) for line in section_b.splitlines()],
    )


def check_pages(
    list_page_order: list[PageOrder], list_pages: list[list[Page]]
) -> Iterator[tuple[bool, list[Page]]]:
    for pages in list_pages:
        yield all(
            (b, a) not in list_page_order for a, b in itertools.combinations(pages, 2)
        ), pages


def part1(input: str) -> int:
    list_page_order, list_pages = parse_input(input)

    return sum(
        pages[len(pages) // 2]
        for is_correct, pages in check_pages(list_page_order, list_pages)
        if is_correct
    )


def part2(input: str) -> int:
    list_page_order, list_pages = parse_input(input)

    middle = 0

    G = nx.DiGraph(list_page_order)

    for is_correct, pages in check_pages(list_page_order, list_pages):
        if is_correct:
            continue

        nodes: Counter[Page] = collections.Counter()

        for a, b in itertools.product(pages, repeat=2):
            with contextlib.suppress(nx.NetworkXNoPath):
                nodes[a] += nx.shortest_path_length(G, a, b)
        else:
            correct_path = sorted(nodes, key=lambda i: nodes[i], reverse=True)

            middle += correct_path[len(pages) // 2]

    return middle


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
