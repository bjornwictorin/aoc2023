#!/usr/bin/env python3

from re import search

def main():
    total_steps = 0
    directions = ""
    node_map = {}
    with open("input.txt", "r") as f:
        first_line = True
        pattern = r"(.*) = \((.*), (.*)\)"
        for line in f:
            if first_line:
                directions = line.strip()
                first_line = False
            elif len(line) != 1:
                match = search(pattern, line)
                node_map[match.group(1)] = (match.group(2), match.group(3))
    pos = "AAA"
    while pos != "ZZZ":
        dir = directions[total_steps % len(directions)]
        assert dir in ("L", "R")
        pos = node_map[pos][0] if dir == "L" else node_map[pos][1]
        total_steps += 1
        assert len(pos) == 3, pos
    # print(f"{directions=}")
    # print(f"{node_map=}")
    print(f"{total_steps=}")
            

if __name__ == "__main__":
    main()
