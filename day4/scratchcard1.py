#!/usr/bin/env python3


def main():
    total_points = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.split(": ")[1].strip()
            winning_values, card_values = line.split(" | ")
            winning_values = [int(x) for x in winning_values.split()]
            card_values = [int(x) for x in card_values.split()]
            present_numbers = len([x for x in card_values if x in winning_values])
            card_points = 2 ** (present_numbers - 1) if present_numbers != 0 else 0
            total_points += card_points
    print(f"{total_points=}")

if __name__ == "__main__":
    main()
