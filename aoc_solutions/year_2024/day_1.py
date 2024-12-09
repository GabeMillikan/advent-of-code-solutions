import bisect

from aoc_solutions.framework import BaseDay


class Day(BaseDay):
    def part_one(self) -> str:
        left_locations: list[int] = []
        right_locations: list[int] = []

        with self.input_path.open() as f:
            for line in f:
                left_location, right_location = line.split()

                bisect.insort(left_locations, int(left_location))
                bisect.insort(right_locations, int(right_location))

        return str(sum(abs(l - r) for l, r in zip(left_locations, right_locations)))

    def part_two(self) -> str:
        left_locations: list[str] = []
        right_location_counts: dict[str, int] = {}

        with self.input_path.open() as f:
            for line in f:
                left_location, right_location = line.split()

                left_locations.append(left_location)

                right_location_counts.setdefault(right_location, 0)
                right_location_counts[right_location] += 1

        return str(
            sum(int(l) * right_location_counts.get(l, 0) for l in left_locations),
        )
