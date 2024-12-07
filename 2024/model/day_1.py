# -*- coding: utf-8 -*-

# built-in libraries
from __future__ import annotations

import os
import re
from typing import List, Union

# internal libraries
from interface.iday import IDay, IPart, IPuzzleInput

# installed libraries


class DayInput(IPuzzleInput):
    def __init__(self, file: str):
        super().__init__(file)

    def load(self) -> Union[List[str], List[str]]:
        with open(file=self.file, mode="r", encoding="utf-8") as file:
            puzzle_file = file.read()
            left = re.split("[ ]+[0-9]+\\n?", puzzle_file)[:-1]
            right = re.split("\\n?[0-9]+[ ]+", puzzle_file)[1:]

            left.sort()
            right.sort()

            return left, right


class Part01(IPart):
    def __init__(self, puzzle_input: IPuzzleInput):
        super().__init__(puzzle_input)

    def solve(self):
        left, right = self.puzzle_input.load()

        distance = 0

        for l, r in zip(left, right):
            distance += abs(int(l) - int(r))

        return f"Total distance: {distance}"


class Part02(IPart):
    def __init__(self, puzzle_input: IPuzzleInput = None):
        super().__init__(puzzle_input)

    def solve(self):
        left, right = self.puzzle_input.load()

        left_item_frequency_in_right = {}

        for item in right:
            if item not in left_item_frequency_in_right:
                left_item_frequency_in_right[item] = 1
            else:
                left_item_frequency_in_right[item] += 1

        distance = 0

        for item in left:
            if item in left_item_frequency_in_right:
                distance += int(item) * int(left_item_frequency_in_right[item])

        return f"Total distance: {distance}"


class Day(IDay):
    def __init__(self):
        super().__init__(
            day="01",
            day_input=DayInput(file=os.path.join(".", "model", "inputs", "day_01.txt")),
            all_parts=[Part01, Part02],
        )
