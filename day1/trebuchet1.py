#!/usr/bin/env python3

def find_first_digit(str: str) -> int:
    for char in str:
        if char.isnumeric():
            return int(char)
    assert False

def main():
    calibration_val = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            # print(line)
            first_digit = find_first_digit(line)
            last_digit = find_first_digit(line[::-1])
            calibration_val += 10 * first_digit + last_digit
    print(f"{calibration_val=}")

if __name__ == "__main__":
    main()
