from aoc_solutions import years

for year_number, year in years.items():
    print(f"{year_number}:")
    year.print_results(indent=1)
