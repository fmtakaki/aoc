# -*- coding: utf-8 -*-

# built-in libraries
from __future__ import annotations

import os
import re
from typing import Dict, List, Literal, Union

# internal libraries
from interface.iday import IDay, IPart, IPuzzleInput, DayError

# installed libraries


class DayInput(IPuzzleInput):
    def __init__(self, file: str):
        super().__init__(file)

    def load(self) -> List[str]:
        with open(file=self.file, mode="r", encoding="utf-8") as file:
            return file.readlines()


class Part01(IPart):
    def __init__(self, puzzle_input: IPuzzleInput = None):
        super().__init__(puzzle_input)

    def solve(self):
        safe_reports = 0
        for line in self.puzzle_input.load():
            l = line.replace("\n", "").split(" ")

            level_evaluator = lambda x: x == 0 or x > 3
            level_dif = [
                level_evaluator(abs(int(j) - int(i))) for i, j in zip(l, l[1:])
            ]

            if True not in level_dif:
                level_direction = lambda x: -1 if x < 0 else 1
                level_dif = sum(
                    [level_direction(int(i) - int(j)) for i, j in zip(l, l[1:])]
                )

                if level_dif == (len(l) - 1) * -1 or level_dif == (len(l) - 1):
                    safe_reports += 1

        return f"Total safe reports: {safe_reports}"  # Right answer: 534


class Part02(IPart):
    def __init__(self, puzzle_input: IPuzzleInput):
        pass

    def solve(self):
        return super().solve()


class Day(IDay):
    def __init__(self):
        super().__init__(
            day="02",
            day_input=DayInput(file=os.path.join(".", "model", "inputs", "day_02.txt")),
            all_parts=[Part01, Part02],
        )
