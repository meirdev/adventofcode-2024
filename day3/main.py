import re


def parse_input(input: str) -> str:
    return input.strip()


def part1(input: str) -> int:
    return sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", input))


def part2(input: str) -> int:
    sum, last_do = 0, True

    for i in re.finditer(r"(do)\(\)|(don't)\(\)|(mul)\((\d+),(\d+)\)", input):
        do, do_not, mul, a, b = i.groups()

        if do is not None:
            last_do = True

        if do_not is not None:
            last_do = False

        if mul is not None and last_do:
            sum += int(a) * int(b)

    return sum


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
