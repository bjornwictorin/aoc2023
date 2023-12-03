#!/usr/bin/env python3

def is_symbol(char: str) -> bool:
    assert len(char) == 1
    return not (char.isnumeric() or char == ".")

def main():
    part_sum = 0
    lines = []
    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line.strip())    
    num_lines = len(lines)
    gear2part = {}
    for line_index in range(num_lines):
        current_line: str = "." + lines[line_index] + "."
        # Add padding line with only dots before first and after last row
        prev_line = "." + lines[line_index - 1] + "." if line_index > 0 else "." * len(current_line)
        next_line = "." + lines[line_index + 1] + "." if line_index < num_lines - 1 else "." * len(current_line)
        # Keep track of state
        part_value = 0
        part_value_len = 0
        symbol_neighbor = False
        for pos, char in enumerate(current_line):
            if char.isnumeric():
                # Check to the left
                if (pos > 0 and is_symbol(current_line[pos - 1]) or is_symbol(prev_line[pos - 1]) or is_symbol(next_line[pos - 1])):
                    symbol_neighbor = True
                # Check to the right
                elif pos < len(current_line) - 1 and (is_symbol(current_line[pos + 1]) or is_symbol(prev_line[pos + 1]) or is_symbol(next_line[pos + 1])):
                    symbol_neighbor = True
                # Check above and below
                elif is_symbol(prev_line[pos]) or is_symbol(next_line[pos]):
                    symbol_neighbor = True
                part_value = 10 * part_value + int(char)
                part_value_len += 1
            elif part_value != 0:
                if symbol_neighbor:
                    part_sum += part_value
                # add part in all adjacent gears lists
                for gear_x in range(pos - part_value_len - 1, pos + 1):
                    if prev_line[gear_x] == "*":
                        gear_pos = (gear_x, line_index - 1) 
                        if gear_pos in gear2part:
                            gear2part[gear_pos].append(part_value)
                        else:
                            gear2part[gear_pos] = [part_value]
                    if current_line[gear_x] == "*":
                        gear_pos = (gear_x, line_index) 
                        if gear_pos in gear2part:
                            gear2part[gear_pos].append(part_value)
                        else:
                            gear2part[gear_pos] = [part_value]
                    if next_line[gear_x] == "*":
                        gear_pos = (gear_x, line_index + 1)
                        if gear_pos in gear2part:
                            gear2part[gear_pos].append(part_value)
                        else:
                            gear2part[gear_pos] = [part_value]
                # reset state
                part_value = 0
                part_value_len = 0
                symbol_neighbor = False
    print(f"{part_sum=}")
    # print(f"{gear2part=}")
    gear_ratio_sum = sum([part_list[0] * part_list[1] for part_list in gear2part.values() if len(part_list) == 2])
    print(f"{gear_ratio_sum=}")


if __name__ == "__main__":
    main()
