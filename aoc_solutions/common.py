from abc import ABC, abstractmethod
from pathlib import Path
from typing import TypeVar


class BaseDay(ABC):
    def __init__(self, input_path: Path) -> None:
        self.input_path = input_path

    @abstractmethod
    def part_one(self) -> str: ...

    @abstractmethod
    def part_two(self) -> str: ...


ConcreteDay = TypeVar("ConcreteDay", bound=BaseDay)


class Year:
    def __init__(self, year: int, days: dict[int, type[ConcreteDay]]) -> None:
        self.year = year
        self.days = days

    def input_file_for_day(self, year: int, day: int) -> Path:
        return Path("aoc_input") / str(year) / f"{day:02d}.txt"

    def print_results(self, *, indent: int = 0, indent_using: str = "  ") -> None:
        for day_number, Day in self.days.items():
            print(f"{indent * indent_using}Day {day_number}:")

            solution = Day(self.input_file_for_day(self.year, day_number))

            print(f"{(indent + 1) * indent_using}Part 1: {solution.part_one()}")
            print(f"{(indent + 1) * indent_using}Part 2: {solution.part_two()}")


__all__ = ["BaseDay", "Year"]
