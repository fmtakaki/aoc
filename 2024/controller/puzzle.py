# -*- coding: utf-8 -*-

# built-in libraries
from __future__ import annotations

import importlib
from typing import Literal, Union

# internal libraries
from interface.iday import IDay

# installed libraries


class PuzzleError(Exception):
    pass


class Puzzle:
    def __init__(self, day: Union[int, Literal["all"]]) -> None:
        try:
            mdl = importlib.import_module(f"model.day_{day}")
            self.day_puzzle: IDay = getattr(mdl, "Day")()
        except ImportError as err:
            raise PuzzleError(
                f"It looks like the Day {day} puzzle is not implemented yet."
            ) from err

    def solve(self, part: Union[int, Literal["all"]]) -> None:
        self.day_puzzle.solve(part)
