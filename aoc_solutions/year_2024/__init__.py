from aoc_solutions.framework import Year

from . import day_1, day_2, day_3, day_4

days = {
    1: day_1.Day,
    2: day_2.Day,
    3: day_3.Day,
    4: day_4.Day,
}
year = Year(2024, days)

__all__ = ["days", "year"]
