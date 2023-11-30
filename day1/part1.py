#!/usr/bin/env python3

def main():
    with open("test_input.txt", "r") as f:
        for line in f:
            line = line.strip()
            print(line)


if __name__ == "__main__":
    main()
