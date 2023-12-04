#!/usr/bin/env python3

def calc_points(line: str) -> int:
    line = line.split(": ")[1].strip()
    winning_values, card_values = line.split(" | ")
    winning_values = [int(x) for x in winning_values.split()]
    card_values = [int(x) for x in card_values.split()]
    return len([x for x in card_values if x in winning_values])

def main():
    # Change to match number of lines in input file
    num_indices = 220
    cards_per_index = num_indices * [1]
    with open("input.txt", "r") as f:
        for index, line in enumerate(f):
            present_numbers = calc_points(line)
            for ii in range(index + 1, index + 1 + present_numbers):
                cards_per_index[ii] += cards_per_index[index]
            
    total_cards = sum(cards_per_index)
    print(f"{total_cards=}")
    

if __name__ == "__main__":
    main()
