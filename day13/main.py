import dataclasses
import re

import sympy  # type: ignore


@dataclasses.dataclass
class ClawMachine:
    button_a_x: int
    button_a_y: int
    button_b_x: int
    button_b_y: int
    prize_x: int
    prize_y: int


def parse_input(input: str) -> list[ClawMachine]:
    return list(
        map(
            lambda i: ClawMachine(*map(int, i)),
            re.findall(
                r"Button A: X\+(?P<ax>\d+), Y\+(?P<ay>\d+)\s+Button B: X\+(?P<bx>\d+), Y\+(?P<by>\d+)\s+Prize: X=(?P<px>\d+), Y=(?P<py>\d+)",
                input,
                re.MULTILINE,
            ),
        )
    )


def solution(input: str, prize_factor: int) -> int:
    claw_machines = parse_input(input)

    sum = 0

    for i in claw_machines:
        i.prize_x += prize_factor
        i.prize_y += prize_factor

        x, y = sympy.symbols("x y", integer=True)

        tokens = [
            i[x] * 3 + i[y] * 1
            for i in sympy.solve(
                [
                    x * i.button_a_x + y * i.button_b_x - i.prize_x,
                    x * i.button_a_y + y * i.button_b_y - i.prize_y,
                ],
                [x, y],
                dict=True,
            )
        ]

        if len(tokens) > 0:
            sum += min(tokens)

    return sum


def part1(input: str) -> int:
    return solution(input, 0)


def part2(input: str) -> int:
    return solution(input, 10000000000000)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
