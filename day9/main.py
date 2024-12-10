import itertools
from dataclasses import dataclass
from typing import cast


@dataclass
class Block:
    size: int


@dataclass
class File(Block):
    size: int
    id: int


@dataclass
class FreeSpace(Block):
    size: int


def parse_input(input: str) -> str:
    return input.strip()


def get_disk(disk_map: str) -> list[Block]:
    disk: list[Block] = []

    block: type[Block] = File
    id = 0

    for value in disk_map:
        n = int(value)

        if block == File:
            disk.append(File(size=n, id=id))
            block = FreeSpace
            id += 1
        else:
            disk.append(FreeSpace(size=n))
            block = File

    return disk


def flatten_blocks(disk: list[Block]) -> list[int | None]:
    return list(
        itertools.chain.from_iterable(
            ([i.id] if isinstance(i, File) else [None]) * i.size for i in disk  # type: ignore
        )
    )


def sum_blocks(files: list[int | None]) -> int:
    return sum(i * file for i, file in enumerate(files) if file is not None)


def part1(input: str) -> int:
    disk_map = parse_input(input)

    disk = get_disk(disk_map)

    files = flatten_blocks(disk)

    free_space_index = 0
    file_index = len(files) - 1

    while True:
        try:
            free_space_index = files.index(None, free_space_index)
        except ValueError:
            break

        try:
            file_index = next(
                i
                for i in range(file_index, free_space_index, -1)
                if files[i] is not None
            )
        except StopIteration:
            break
        else:
            value = files.pop(file_index)
            files[free_space_index] = value

            file_index -= 1

    return sum_blocks(files)


def part2(input: str) -> int:
    disk_map = parse_input(input)

    disk = get_disk(disk_map)

    for i in range(len(disk) - 1, -1, -1):
        for j in range(i):
            if (
                isinstance(disk[i], File)
                and isinstance(disk[j], FreeSpace)
                and disk[i].size <= disk[j].size
            ):
                file = cast(File, disk[i])
                id, size = file.id, file.size

                disk[i] = FreeSpace(size)
                disk[j] = FreeSpace(disk[j].size - size)

                disk.insert(j, File(size=size, id=id))

    return sum_blocks(flatten_blocks(disk))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
