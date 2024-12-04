import re

from aoc_solutions.common import BaseDay


class Day(BaseDay):
    def part_one(self) -> str:
        with self.input_path.open() as f:
            return str(
                sum(
                    int(m.group(1)) * int(m.group(2))
                    for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", f.read())
                ),
            )

    def part_two(self) -> str:
        with self.input_path.open() as f:
            total = 0
            enabled = True
            for m in re.finditer(
                r"do(?:n't)?\(\)|mul\((\d{1,3}),(\d{1,3})\)",
                f.read(),
            ):
                if m.group() == "do()":
                    enabled = True
                elif m.group() == "don't()":
                    enabled = False
                elif enabled:
                    total += int(m.group(1)) * int(m.group(2))

            return str(total)
