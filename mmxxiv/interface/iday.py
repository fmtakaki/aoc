# -*- coding: utf-8 -*-

# built-in libraries
from __future__ import annotations

import os

from abc import ABCMeta, abstractmethod
from typing import Any, List, Literal, Union

# internal libraries

# installed libraries


class DayError(Exception):
    pass


class IPuzzleInput(metaclass=ABCMeta):
    def __init__(self, file: str) -> None:
        if not os.path.isfile(file):
            raise FileNotFoundError(
                f"The puzzle file '{file}' cannot be found {os.path.abspath(os.path.curdir)}"
            )

        self.file = file

    @abstractmethod
    def load(self) -> Any: ...


class IPart(metaclass=ABCMeta):
    def __init__(self, puzzle_input: IPuzzleInput):
        self.puzzle_input: IPuzzleInput = puzzle_input

    @abstractmethod
    def solve(self) -> str: ...


class IDay(metaclass=ABCMeta):
    def __init__(self, day: str, day_input: str, all_parts: List[IPart]):
        self.day: str = day
        self.all_parts: List[IPart] = [
            part(puzzle_input=day_input) for part in all_parts
        ]

    def solve(self, part: Union[int, Literal["all"]]) -> bool:
        if str(part) == "all":
            for part_index, part_obj in enumerate(self.all_parts):
                print(f"Day {self.day}, Part {part_index+1}, Answer {part_obj.solve()}")
            return True

        if isinstance(part, int) and part - 1 >= 0 and part - 1 < len(self.all_parts):
            print(
                f"Day {self.day}, Part {part}, Answer {self.all_parts[part-1].solve()}"
            )
            return True

        raise DayError(
            f"The Day {self.day} does not have Part {part} or it was not implemented yet"
        )
