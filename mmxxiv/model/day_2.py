# -*- coding: utf-8 -*-

# built-in libraries
from __future__ import annotations

import os
from collections import UserList
from typing import Any, Dict, List

# internal libraries
from interface.iday import IDay, IPart, IPuzzleInput
from model.settings import *

# installed libraries


class DayInput(IPuzzleInput):
    def __init__(self, file: str):
        super().__init__(file)

    def load(self) -> List[str]:
        with open(file=self.file, mode="r", encoding="utf-8") as file:
            return file.readlines()


class Report(UserList):
    def __init__(self, report: List[int] = None, threshold: int = 0):
        report = [int(level) for level in report]
        super().__init__(report)

        self._detail = {
            "summary": {
                "no_of_direction_changes": 0,
                "no_of_out_of_range": 0,
                "direction_trend": 0,
            },
            "details_by_index": {},
        }

        if report is not None:
            self.__detail(report)

        self.is_safe = (
            (self.no_of_direction_changes == 0 and self.no_of_out_of_range == 0)
            or (
                self.no_of_direction_changes <= threshold
                and self.no_of_out_of_range == 0
            )
            or (
                self.no_of_direction_changes == 0
                and self.no_of_out_of_range <= threshold
            )
        )

    def __detail(self, report: List[int]):
        previous_direction = 0
        current_direction = 0
        out_of_range = None
        level_dir = lambda x: 1 if x < 0 else -1 if x > 0 else 0
        level_is_out_of_range = lambda x: x == 0 or x > 3 or x < -3
        index = 0
        direction_trend = 0

        for x, y in zip(report, report[1:]):
            current_direction = level_dir(x - y)
            if (
                previous_direction != 0
                and previous_direction != current_direction
                and current_direction != 0
            ):
                self._detail["summary"]["no_of_direction_changes"] += 1

            previous_direction = current_direction
            direction_trend += current_direction

            out_of_range = level_is_out_of_range(x - y)
            self._detail["summary"]["no_of_out_of_range"] += 1 if out_of_range else 0

            self._detail["details_by_index"][index] = {
                "direction": current_direction,
                "out_of_range": out_of_range,
            }
            index += 1

        self._detail["summary"]["direction_trend"] = level_dir(direction_trend * -1)

    @property
    def no_of_direction_changes(self) -> int:
        return self._detail["summary"]["no_of_direction_changes"]

    @property
    def no_of_out_of_range(self) -> int:
        return self._detail["summary"]["no_of_out_of_range"]

    @property
    def direction_change_indexes(self) -> List[int]:
        return self._detail["unsafe_indexes"]["direction_change"]

    @property
    def direction_trend(self) -> int:
        return self._detail["summary"]["direction_trend"]


class Part01(IPart):
    def __init__(self, puzzle_input: IPuzzleInput = None):
        super().__init__(puzzle_input)

    def report_analyzer(self) -> Dict[str, Any]:
        reports = {"safe": [], "unsafe": []}

        for line in self.puzzle_input.load():
            l = line.replace("\n", "").split(" ")
            report = Report(l)

            if report.is_safe:
                reports["safe"].append(report)
            else:
                reports["unsafe"].append(report)

        return reports

    def solve(self) -> str:
        return f"Total safe reports: {len(self.report_analyzer()['safe'])}"  # Right answer: 534


class Part02(IPart):
    def __init__(self, puzzle_input: IPuzzleInput):
        super().__init__(puzzle_input)

    def solve(self) -> str:
        """
        This methos is not solving the problem correclty. It should be reviewed later.
        """
        p1 = Part01(puzzle_input=self.puzzle_input)
        reports = p1.report_analyzer()
        converted_report_to_safe = {"reports": {}, "qty": 0}
        converted_report_to_safe_by_dr = {"reports": {}, "qty": 0}
        converted_report_to_safe_by_oor = {"reports": {}, "qty": 0}

        for report in reports["unsafe"]:
            # converted = False
            rpt = Report(report, 10)

            if not rpt.is_safe:
                continue

            index = 0
            level_dir = lambda x: 1 if x < 0 else -1 if x > 0 else 0
            level_oor = lambda x, y: abs(x - y) >= 1 and abs(x - y) <= 3
            for x, y, z in zip(report, report[1:], report[2:]):
                first_pair = level_dir(x - y)
                second_pair = level_dir(y - z)

                if (
                    first_pair == rpt.direction_trend
                    and second_pair == rpt.direction_trend
                ):
                    # index += 1
                    continue

                if (
                    first_pair != rpt.direction_trend
                    and second_pair == rpt.direction_trend
                ):
                    break

                if (
                    first_pair == rpt.direction_trend
                    and second_pair != rpt.direction_trend
                ):
                    index += 2
                    break

                first_pair = level_oor(x, y)
                second_pair = level_oor(y, z)

                if first_pair and second_pair:
                    # index += 1
                    continue

                if first_pair and not second_pair:
                    index += 2
                    break

                if not first_pair and second_pair:
                    break

                if not first_pair and not second_pair:
                    index = +1
                    break

                index += 1

            # direction_change_index = rpt.direction_change_indexes[0]
            temp_rpt = report.copy()
            del temp_rpt[index]
            temp_report = Report(temp_rpt)
            # print(f">> {temp_report}, {temp_report.is_safe}")
            if temp_report.is_safe:
                idx = converted_report_to_safe["qty"] + 1
                converted_report_to_safe["qty"] = idx
                converted_report_to_safe["reports"][idx] = {}
                converted_report_to_safe["reports"][idx]["before"] = report
                converted_report_to_safe["reports"][idx]["after"] = temp_report
                # converted = True
            else:
                print(temp_report)

            # if rpt.no_of_out_of_range == 2:
            # print(report, end="")
            # if not converted:
            #     index = 0
            #     for x, y, z in zip(report, report[1:], report[2:]):
            #         first_pair = abs(x - y) >= 1 and abs(x - y) <= 3
            #         second_pair = abs(y - z) >= 1 and abs(y - z) <= 3

            #         if first_pair and second_pair:
            #             index += 1
            #             continue

            #         if first_pair and not second_pair:
            #             index += 2
            #             break

            #         if not first_pair and second_pair:
            #             break

            #         if not first_pair and not second_pair:
            #             index = +1
            #             break

            #     temp_rpt = report.copy()
            #     del temp_rpt[index]
            #     temp_report = Report(temp_rpt)

            #     if temp_report.is_safe:
            #         idx = converted_report_to_safe_by_oor["qty"] + 1
            #         converted_report_to_safe_by_oor["qty"] = idx
            #         converted_report_to_safe_by_oor["reports"][idx] = {}
            #         converted_report_to_safe_by_oor["reports"][idx]["before"] = report
            #         converted_report_to_safe_by_oor["reports"][idx][
            #             "after"
            #         ] = temp_report
            #         # print(f"OOR={report}")
            #     else:
            #         print(f"OOR={report}")

        return f"Total safe reports: {len(reports['safe'])}+{converted_report_to_safe['qty']}={len(reports['safe'])+converted_report_to_safe['qty']}"  # Right answer: 577


class Day(IDay):
    def __init__(self):
        super().__init__(
            day="02",
            day_input=DayInput(file=os.path.join(PUZZLE_INPUT_PATH, "day_02.txt")),
            all_parts=[Part01, Part02],
        )
