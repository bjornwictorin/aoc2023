#!/usr/bin/env python3

from re import findall
from typing import List, Tuple

def remap_entry(entry: int, table: List[Tuple[int, int, int]]) -> int:
    # print(f"{table=}")
    new_entry = entry # by default values map to themselves
    for src_start, dst_start, range_len in table:
        if src_start <= entry < src_start + range_len:
            new_entry = dst_start + (entry - src_start)
            break
    return new_entry


def apply_all_tables(entry: int, tables: List[List[Tuple[int, int, int]]]) -> int:
    for table in tables:
        entry = remap_entry(entry, table)
    return entry

def main():
    seeds = []
    translation_table = []
    with open("input.txt", "r") as f:
        for line in f:
            if line.startswith("seeds"):
                seeds.extend([int(x) for x in findall(r"\d+", line)])
            elif "map" in line:
                # add new translation table section
                translation_table.append([])
            elif line[0].isnumeric():
                # add range to translation table section
                numbers = tuple(int(x) for x in findall(r"\d+", line))
                assert len(numbers) == 3
                translation_table[-1].append(numbers)
            else:
                assert len(line) == 1 # only newline
    print(f"{seeds=}")

    # search backwards, from location to seed
    translation_table = translation_table[::-1]

    location = -1
    seed_found = False
    while not seed_found:
        location += 1
        seed = apply_all_tables(location, translation_table)
        # if seed in seeds:
        #     seed_found = True
        if location % 10000000 == 0:
            print(location)
        range_start = 0
        for ii, val in enumerate(seeds):
            if ii % 2 == 0:
                range_start = val
            else:
                range_end = range_start + val
                if seed in range(range_start, range_end):
                    seed_found = True
                    break
    print(location)


if __name__ == "__main__":
    main()
