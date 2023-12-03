#!/usr/bin/env python3

def is_symbol(char: str) -> bool:
    assert len(char) == 1
    return not (char.isnumeric() or char == "." or char == "\n")

def main():
    part_sum = 0
    lines = []
    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line)    
    num_lines = len(lines)
    line_width = len(lines[0])
    padding_line = "." * line_width
    for line_index in range(num_lines):
        current_line: str = lines[line_index]
        # Add padding line with only dots before first and after last row
        prev_line = lines[line_index - 1] if line_index > 0 else padding_line
        next_line = lines[line_index + 1] if line_index < num_lines - 1 else padding_line
        # Keep track of state
        part_value = 0
        part_value_len = 0
        symbol_neighbor = False
        for pos, char in enumerate(current_line):
            if char.isnumeric():
                # Check to the left
                if pos > 0 and (is_symbol(current_line[pos - 1]) or is_symbol(prev_line[pos - 1]) or is_symbol(next_line[pos - 1])):
                    symbol_neighbor = True
                # Check to the right
                elif pos < line_width - 1 and (is_symbol(current_line[pos + 1]) or is_symbol(prev_line[pos + 1]) or is_symbol(next_line[pos + 1])):
                    symbol_neighbor = True
                # Check above and below
                elif is_symbol(prev_line[pos]) or is_symbol(next_line[pos]):
                    symbol_neighbor = True
                part_value = 10 * part_value + int(char)
                part_value_len += 1
            elif part_value != 0:
                print(f"{part_value=}")
                if symbol_neighbor:
                    part_sum += part_value
                # reset state
                part_value = 0
                part_value_len = 0
                symbol_neighbor = False
    print(f"{part_sum=}")

if __name__ == "__main__":
    main()
