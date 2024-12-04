import itertools


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()


def part1(input: str) -> int:
    lines = parse_input(input)

    word = "XMAS"

    words = [word, word[::-1]]

    return len(
        set(
            tuple(sorted(letters))
            for y in range(len(lines))
            for x in range(len(lines[y]))
            for i, j in itertools.product((-1, 0, 1), repeat=2)
            if (
                letters := [
                    (y + i * k, x + j * k)
                    for k in range(len(word))
                    if 0 <= y + i * k < len(lines)
                    and 0 <= x + j * k < len(lines[y + i * k])
                ]
            )
            and "".join([lines[a][b] for a, b in letters]) in words
        )
    )


def part2(input: str) -> int:
    lines = parse_input(input)

    words = [["M", "A", "S"], ["S", "A", "M"]]

    return sum(
        [lines[y - 1][x - 1], lines[y][x], lines[y + 1][x + 1]] in words
        and [lines[y - 1][x + 1], lines[y][x], lines[y + 1][x - 1]] in words
        for y in range(1, len(lines) - 1)
        for x in range(1, len(lines[y]) - 1)
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
