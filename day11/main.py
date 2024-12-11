import collections
from typing import Counter


def parse_input(input: str) -> list[str]:
    return input.strip().split(" ")


def blink(stones: Counter[str]) -> Counter[str]:
    new_stones: Counter[str] = collections.Counter()

    for stone, n in stones.items():
        if stone == "0":
            new_stones["1"] += n
        else:
            if len(stone) % 2 == 0:
                m = len(stone) // 2

                stone_a = stone[:m]

                stone_b = stone[m:].lstrip("0")
                if stone_b == "":
                    stone_b = "0"

                new_stones[stone_a] += n
                new_stones[stone_b] += n
            else:
                new_stones[str(int(stone) * 2024)] += n

    return new_stones


def solution(input: str, blinks: int) -> int:
    stones = parse_input(input)

    stones_counter = collections.Counter(stones)

    for _ in range(blinks):
        stones_counter = blink(stones_counter)

    return stones_counter.total()


def part1(input: str) -> int:
    return solution(input, 25)


def part2(input: str) -> int:
    return solution(input, 75)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
