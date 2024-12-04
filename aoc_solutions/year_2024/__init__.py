from aoc_solutions.common import Year

from . import day_1, day_2, day_3

days = {
    1: day_1.Day,
    2: day_2.Day,
    3: day_3.Day,
}
year = Year(2024, days)

__all__ = ["days", "year"]
