from aoc_solutions.common import BaseDay


class Day(BaseDay):
    def part_one(self) -> str:
        with self.input_path.open() as f:
            rows = f.read().splitlines()

        n_rows = len(rows)
        n_cols = len(rows[0])

        xmas_found = 0

        for y in range(n_rows):
            for x in range(n_cols):
                horizontal = rows[y][x : x + 4]
                vertical = "".join(row[x] for row in rows[y : y + 4])
                diagonal_se = "".join(
                    rows[y + i][x + i]
                    for i in range(4)
                    if y + i < n_rows and x + i < n_cols
                )
                diagonal_ne = "".join(
                    rows[y - i][x + i]
                    for i in range(4)
                    if y - i >= 0 and x + i < n_cols
                )

                for string in horizontal, vertical, diagonal_ne, diagonal_se:
                    if string in {"XMAS", "SAMX"}:
                        xmas_found += 1

        return str(xmas_found)

    def part_two(self) -> str:
        with self.input_path.open() as f:
            rows = f.read().splitlines()

        n_rows = len(rows)
        n_cols = len(rows[0])

        x_mas_found = 0

        for y in range(n_rows - 2):
            for x in range(n_cols - 2):
                diagonal_se = "".join(rows[y + i][x + i] for i in range(3))
                diagonal_sw = "".join(rows[y + i][x + 2 - i] for i in range(3))

                if diagonal_se in {"MAS", "SAM"} and diagonal_sw in {"MAS", "SAM"}:
                    x_mas_found += 1

        return str(x_mas_found)
