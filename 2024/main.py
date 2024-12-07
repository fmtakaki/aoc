# -*- coding: utf-8 -*-

# built-in libraries
from __future__ import annotations

from typing import Literal, Union

# internal libraries
from controller.puzzle import Puzzle

# installed libraries
import typer


app = typer.Typer(no_args_is_help=True)


@app.command()
def solve(day: int = None, part: int = None) -> None:
    puzzle = Puzzle(day="all" if day is None else day)
    puzzle.solve(part="all" if part is None else part)


if __name__ == "__main__":
    app()
