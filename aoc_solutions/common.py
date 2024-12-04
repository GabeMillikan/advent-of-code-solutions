from pathlib import Path
from typing import Literal, overload


class BaseDay:
    def __init__(self, input_path: Path) -> None:
        self.input_path = input_path

    def part_one(self) -> str:
        return "No solution implemented."

    def part_two(self) -> str:
        return "No solution implemented."


class Year:
    def __init__(self, year: int, days: dict[int, type[BaseDay]]) -> None:
        self.year = year
        self.days = days

    def input_file_for_day(self, year: int, day: int) -> Path:
        return Path("aoc_input") / str(year) / f"{day:02d}.txt"

    @overload
    def print_results(
        self,
        *,
        indent: int = 0,
        indent_using: str = "  ",
        only_day: int | None = None,
    ) -> None: ...

    @overload
    def print_results(
        self,
        *,
        indent: int = 0,
        indent_using: str = "  ",
        only_day: int,
        only_part: Literal[1, 2] | None = None,
    ) -> None: ...

    def print_results(
        self,
        *,
        indent: int = 0,
        indent_using: str = "  ",
        only_day: int | None = None,
        only_part: Literal[1, 2] | None = None,
    ) -> None:
        if only_day is not None:
            Day = self.days[only_day]
            solution = Day(self.input_file_for_day(self.year, only_day))

            if only_part == 1:
                print(f"{indent * indent_using}{solution.part_one()}")
            elif only_part == 2:
                print(f"{indent * indent_using}{solution.part_two()}")
            else:
                print(f"{indent * indent_using}Part 1: {solution.part_one()}")
                print(f"{indent * indent_using}Part 2: {solution.part_two()}")

            return

        assert only_part is None, "Cannot specify a certain part without a certain day."

        for day_number in self.days:
            print(f"{indent * indent_using}Day {day_number}:")
            self.print_results(
                indent=indent + 1,
                indent_using=indent_using,
                only_day=day_number,
            )


__all__ = ["BaseDay", "Year"]
