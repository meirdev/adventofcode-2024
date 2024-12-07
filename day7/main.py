import collections
import functools
import itertools
from enum import StrEnum
from typing import NamedTuple

import more_itertools


class Equation(NamedTuple):
    result: int
    values: tuple[int, ...]


class Operator(StrEnum):
    ADD = "+"
    MULTIPLY = "*"
    CONCATENATION = "||"


OPERATORS_1 = (Operator.ADD, Operator.MULTIPLY)

OPERATORS_2 = (Operator.ADD, Operator.MULTIPLY, Operator.CONCATENATION)


def parse_input(input: str) -> list[Equation]:
    equations: list[Equation] = []

    for line in input.strip().splitlines():
        result, values = line.split(": ")

        equations.append(
            Equation(
                result=int(result),
                values=tuple(map(int, values.split(" "))),
            )
        )

    return equations


@functools.cache
def can_solve_equation(equation: Equation, operators: tuple[Operator, ...]) -> bool:
    for i in itertools.product(operators, repeat=len(equation.values) - 1):
        equation_elements = collections.deque(
            more_itertools.interleave_longest(equation.values, i)
        )

        while len(equation_elements) >= 3:
            a, o, b = (
                equation_elements.popleft(),
                equation_elements.popleft(),
                equation_elements.popleft(),
            )

            if o == Operator.CONCATENATION:
                equation_elements.appendleft(eval(f"{a}{b}"))
            else:
                equation_elements.appendleft(eval(f"{a}{o}{b}"))

        if equation_elements[0] == equation.result:
            return True

    return False


def part1(input: str) -> int:
    equations = parse_input(input)

    return sum(
        equation.result
        for equation in equations
        if can_solve_equation(equation, OPERATORS_1)
    )


def part2(input: str) -> int:
    equations = parse_input(input)

    can_solve = {
        equation: can_solve_equation(equation, OPERATORS_1) for equation in equations
    }

    for equation in can_solve:
        if not can_solve[equation]:
            can_solve[equation] = can_solve_equation(equation, OPERATORS_2)

    return sum(i.result for i in can_solve if can_solve[i])


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
