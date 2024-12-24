# -*- coding: utf-8 -*-

# built-in libraries
from __future__ import annotations

import os
import re
from typing import List, Union

# internal libraries
from interface.iday import IDay, IPart, IPuzzleInput
from model.settings import *

# installed libraries


class DayInput(IPuzzleInput):
    def __init__(self, file: str):
        super().__init__(file)

    def load(self) -> Union[List[str], List[str]]:
        with open(file=self.file, mode="r", encoding="utf-8") as file:
            return None


class Part01(IPart):
    def __init__(self, puzzle_input: IPuzzleInput):
        super().__init__(puzzle_input)

    def solve(self) -> str:
        return ""


class Part02(IPart):
    def __init__(self, puzzle_input: IPuzzleInput = None):
        super().__init__(puzzle_input)

    def solve(self) -> str:
        return ""


class Day(IDay):
    def __init__(self):
        super().__init__(
            day="xx",
            day_input=DayInput(file=os.path.join(PUZZLE_INPUT_PATH, "day_xx.txt")),
            all_parts=[Part01, Part02],
        )
