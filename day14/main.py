import collections
import dataclasses
import itertools
import math
import re
from typing import Counter, DefaultDict

from PIL import Image

HEIGHT = 103
WIDTH = 101


@dataclasses.dataclass
class Robot:
    position_x: int
    position_y: int
    velocity_x: int
    velocity_y: int

    def move(self, max_height: int, max_width: int) -> None:
        self.position_x = (self.position_x + self.velocity_x) % max_width
        self.position_y = (self.position_y + self.velocity_y) % max_height


def parse_input(input: str) -> list[Robot]:
    return [
        Robot(*map(int, i))
        for i in re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", input)
    ]


def part1(input: str, height: int = HEIGHT, width: int = WIDTH) -> int:
    robots = parse_input(input)

    for _ in range(100):
        for robot in robots:
            robot.move(height, width)

    positions: Counter[tuple[int, int]] = collections.Counter(
        (i.position_y, i.position_x) for i in robots
    )

    quadrants: DefaultDict[tuple[int, int], list[int]] = collections.defaultdict(list)

    height_middle, width_middle = height // 2, width // 2

    for i in positions:
        if i[0] == height_middle or i[1] == width_middle:
            continue

        quadrants[i[0] // (height_middle + 1), i[1] // (width_middle + 1)].append(
            positions[i]
        )

    return math.prod(sum(i) for i in quadrants.values())


def part2(input: str, height: int = HEIGHT, width: int = WIDTH) -> int:
    robots = parse_input(input)

    positions = set()

    for i in itertools.count(1):
        image = Image.new("L", (height + 1, width + 1))

        pixels = []
        for robot in robots:
            robot.move(height, width)
            pixels.append((robot.position_y, robot.position_x))

        pixels_tuple = tuple(pixels)
        if pixels_tuple in positions:
            break
        positions.add(pixels_tuple)

        for pixel in pixels:
            image.putpixel(pixel, 255)
        image.save(f"./images/{i:06}.png")

    # after manually searching for the tree image in the file
    return 8168


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
