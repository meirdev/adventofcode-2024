import re


def parse_input(input: str) -> list[tuple[int, int]]:
    return [(int(a), int(b)) for a, b in re.findall(r"(\d+)\s+(\d+)", input)]


def part1(input: str) -> int:
    numbers = parse_input(input)

    col_a, col_b = zip(*numbers)

    return sum(abs(a - b) for a, b in zip(sorted(col_a), sorted(col_b)))


def part2(input: str) -> int:
    numbers = parse_input(input)

    col_a, col_b = zip(*numbers)

    return sum(a * col_b.count(a) for a in col_a)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
