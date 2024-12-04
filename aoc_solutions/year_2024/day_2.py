from typing import Callable

from aoc_solutions.common import BaseDay


class Day(BaseDay):
    def report_is_safe_1(self, levels: list[int]) -> bool:
        changes = [r - l for l, r in zip(levels, levels[1:])]

        return (
            # low magnitude
            all(1 <= abs(c) <= 3 for c in changes)
            # and all same direction
            and all((c > 0) == (changes[0] > 0) for c in changes[1:])
        )

    def report_is_safe_2(self, levels: list[int]) -> bool:
        # considering that there are never more than like 6 levels,
        # simplicity is preferred over performance
        return any(
            self.report_is_safe_1(levels[:i] + levels[i + 1 :])
            for i in range(len(levels))
        )

    def count_safe_reports(self, criteria: Callable[[list[int]], bool]) -> int:
        total_safe_reports = 0

        with self.input_path.open() as f:
            for report_string in f:
                levels = [int(l) for l in report_string.split()]
                if criteria(levels):
                    total_safe_reports += 1

        return total_safe_reports

    def part_one(self) -> str:
        return str(self.count_safe_reports(self.report_is_safe_1))

    def part_two(self) -> str:
        return str(self.count_safe_reports(self.report_is_safe_2))
