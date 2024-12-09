from aoc_solutions.framework import BaseDay


class Day(BaseDay):
    def parse(self) -> tuple[dict[str, set[str]], list[list[str]]]:
        with self.input_path.open() as f:
            print_keys_after_values = {}
            for line in f:
                line = line.strip()
                if not line:
                    break

                x, y = line.split("|")
                print_keys_after_values.setdefault(y, set())
                print_keys_after_values[y].add(x)

            updates = [update.strip().split(",") for update in f]

        return print_keys_after_values, updates

    def part_one(self) -> str:
        print_keys_after_values, updates = self.parse()

        sum_of_in_order_middles = 0
        for update in updates:
            disallowed_pages = set()

            for page in update:
                if page in disallowed_pages:
                    break

                disallowed_pages.update(print_keys_after_values[page])
            else:
                # valid update!
                middle_page = int(update[len(update) // 2])
                sum_of_in_order_middles += middle_page

        return str(sum_of_in_order_middles)

    def part_two(self) -> str:
        print_keys_after_values, updates = self.parse()

        sum_of_out_of_order_middles = 0
        for update in updates:
            fixed_update = []

            for page in update:
                # push this page as far to the right as it is allowed to go
                i = 0
                while i < len(fixed_update):
                    contender = fixed_update[i]
                    page_must_come_before_contender = (
                        page in print_keys_after_values.get(contender, set())
                    )

                    if page_must_come_before_contender:
                        break

                    i += 1

                fixed_update.insert(i, page)

            if fixed_update != update:
                # a fix was implemented!
                middle_page = int(fixed_update[len(update) // 2])
                sum_of_out_of_order_middles += middle_page

        return str(sum_of_out_of_order_middles)
