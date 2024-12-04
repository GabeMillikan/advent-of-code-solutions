from argparse import ArgumentParser

from aoc_solutions import years

parser = ArgumentParser(description="Process year and day inputs.")
parser.add_argument(
    "year",
    nargs="?",
    type=int,
    default=None,
    help="(optional) The year to execute.",
)
parser.add_argument(
    "day",
    nargs="?",
    type=int,
    choices=list(range(1, 26)),
    default=None,
    help="(optional) The day to execute.",
)
parser.add_argument(
    "part",
    nargs="?",
    type=int,
    choices=[1, 2],
    default=None,
    help="(optional) The part to execute.",
)

args = parser.parse_args()

for year_number, year in years.items():
    if args.year is None:
        print(f"{year_number}:")
    elif year_number != args.year:
        continue

    year.print_results(
        indent=1 if args.year is None else 0,
        only_day=args.day,
        only_part=args.part,
    )
