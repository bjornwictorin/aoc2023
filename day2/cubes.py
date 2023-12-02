#!/usr/bin/env python3

from typing import Tuple


def get_num_color_cubes(game: str) -> Tuple[int, int, int]:
    color_dict = {"red": 0, "green": 0, "blue": 0}
    color_fields = game.split(", ")
    # print(f"{color_fields=}")
    for field in color_fields:
        # print(field)
        tmp = field.split(" ")
        assert len(tmp) == 2, tmp
        num_cubes, color = field.split(" ")
        # print(f"{num_cubes=}, {color=}")
        color_dict[color] = int(num_cubes)
    # print(color_dict)
    return color_dict["red"], color_dict["green"], color_dict["blue"]


def main():
    index_sum = 0
    with open("input.txt", "r") as f:
        for ii, line in enumerate(f):
            line = line.strip().split(": ")[1]
            games = line.split("; ")
            # print(f"{games=}")
            max_red = 0
            max_green = 0
            max_blue = 0
            for game in games:
                red, green, blue = get_num_color_cubes(game)
                max_red = max(max_red, red)
                max_green = max(max_green, green)
                max_blue = max(max_blue, blue)
            if max_red <= 12 and max_green <= 13 and max_blue <= 14:
                index_sum += 1 + ii
    print(f"{index_sum=}")

if __name__ == "__main__":
    main()
