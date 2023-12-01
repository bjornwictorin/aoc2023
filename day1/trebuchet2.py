#!/usr/bin/env python3

from typing import List

def find_first_digit(line: str, numbers: List[str]) -> int:
    index, number = min([(line.find(number), number) for number in numbers if number in line], key = lambda x: x[0])
    assert index != -1
    assert number in numbers
    if number.isnumeric():
        return int(number)
    else:
        assert 0 <= numbers.index(number) <= 9, f"{number=}, {numbers.index(number)=}"
        return numbers.index(number)

def main():
    calibration_val = 0
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] + [str(x) for x in range(10)]
    rev_numbers = [ii[::-1] for ii in numbers]
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            # print(line)
            first_digit = find_first_digit(line, numbers)
            last_digit = find_first_digit(line[::-1], rev_numbers)
            # print(first_digit)
            # print(last_digit)
            calibration_val += 10 * first_digit + last_digit
    print(f"{calibration_val=}")

if __name__ == "__main__":
    main()
