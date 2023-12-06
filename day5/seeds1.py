#!/usr/bin/env python3
from re import findall
from typing import List, Tuple

def apply_table(entries: List[int], table: List[Tuple[int, int, int]]) -> List[int]:
    new_entries = []
    for entry in entries:
        new_entry = entry # by default values map to themselves
        for dst_start, src_start, range_len in table:
            if src_start <= entry < src_start + range_len:
                new_entry = dst_start + (entry - src_start)
                break
        new_entries.append(new_entry)
    assert len(entries) == len(new_entries)
    return new_entries

def main():
    entries = [] # will hold seeds, then soil, then fertilizer, and so on
    translation_table = []
    with open("input.txt", "r") as f:
        for line in f:
            if line.startswith("seeds"):
                seeds = [int(x) for x in findall(r"\d+", line)]
                entries.extend(seeds)
            elif "map" in line:
                # clear translation table
                translation_table.clear()
            elif line[0].isnumeric():
                # add range to translation table
                numbers = tuple(int(x) for x in findall(r"\d+", line))
                assert len(numbers) == 3
                translation_table.append(numbers)
            else:
                assert len(line) == 1 # only newline
                # remember to add one extra blank line at the end of input
                # to trigger this case also after last table
                # apply translation table
                entries = apply_table(entries, translation_table)
    print(f"location: {min(entries)}")

if __name__ == "__main__":
    main()
