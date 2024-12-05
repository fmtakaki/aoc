import re
from typing import List, Union


def load_puzzle_input(puzzle: str, sort: bool = True) -> Union[List[str], List[str]]:
    with open(file=puzzle, mode="r", encoding="utf-8") as file:
        puzzle_file = file.read()
        left = re.split("[ ]+[0-9]+\\n?", puzzle_file)[:-1]
        right = re.split("\\n?[0-9]+[ ]+", puzzle_file)[1:]

        if sort:
            left.sort()
            right.sort()

        return left, right


def main() -> None:
    left, right = load_puzzle_input("input.txt")

    distance = 0

    for l, r in zip(left, right):
        distance += abs(int(l) - int(r))

    print(f"Total distance: {distance}")


if __name__ == "__main__":
    main()
