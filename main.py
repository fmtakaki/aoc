# -*- coding: utf-8 -*-

# built-in libraries
from __future__ import annotations

import os
import sys

# internal libraries


# installed libraries
import typer


app = typer.Typer(no_args_is_help=True)


@app.command()
def solve(year: int = 2024, day: int = None, part: int = None) -> None:
    roman = {2024: "mmxxiv"}

    if year not in roman:
        raise FileNotFoundError(f"The year {year} folder does not exist")

    if not os.path.exists(os.path.join(".", roman[year])):
        raise FileNotFoundError(f"The year {year} folder does not exist")

    sys.path.append(os.path.join(sys.path[0], roman[year]))

    from controller.puzzle import Puzzle

    puzzle = Puzzle(day="all" if day is None else day)
    puzzle.solve(part="all" if part is None else part)


if __name__ == "__main__":
    app()
