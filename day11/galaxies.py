#!/usr/bin/env python3

from typing import Tuple, List

EXPANSION = 1000000

def calc_dist(galaxy: Tuple[int, int], other_galaxy: Tuple[int, int], empty_rows: List[int], empty_columns: List[int]) -> int:
    galaxy_row, galaxy_col = galaxy
    other_galaxy_row, other_galaxy_col = other_galaxy
    passed_empty_rows = len([ii for ii in empty_rows if min(galaxy_row, other_galaxy_row) < ii < max(galaxy_row, other_galaxy_row)])
    passed_empty_cols = len([ii for ii in empty_columns if min(galaxy_col, other_galaxy_col) < ii < max(galaxy_col, other_galaxy_col)])
    return abs(galaxy_row - other_galaxy_row) + abs(galaxy_col - other_galaxy_col) + (EXPANSION - 1) * (passed_empty_cols + passed_empty_rows)


def main():
    distances = []
    space_map = []
    empty_rows = []
    empty_columns = []
    galaxies = []
    with open("input.txt", "r") as f:
        for ii, line in enumerate(f):
            if "#" not in line:
                empty_rows.append(ii)
            space_map.append(line.strip())
    # find empty columns
    for col in range(len(space_map[0])):
        if all(row[col] == "." for row in space_map):
            empty_columns.append(col)
    
    # find galaxies
    for row_index, row in enumerate(space_map):
        for col_index, char in enumerate(row):
            if char == "#":
                galaxies.append((row_index, col_index))
    
    # calculate distances
    for ii, galaxy in enumerate(galaxies):
        for other_galaxy_index in range(ii + 1, len(galaxies)):
            other_galaxy = galaxies[other_galaxy_index]
            distances.append(calc_dist(galaxy, other_galaxy, empty_rows, empty_columns))
            # print(f"{galaxy=} -> {other_galaxy=}: {distances[-1]}")

    print(sum(distances))
            

if __name__ == "__main__":
    main()
