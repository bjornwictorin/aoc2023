#!/usr/bin/env python3


def main():
    race_time = 48938595
    record_distance = 296192812361391
    shortest_hold_time = 0
    longest_hold_time = 0
    # Find first hold time to result in a win
    hold_time = 1
    while True:
        if hold_time * (race_time - hold_time) > record_distance:
            shortest_hold_time = hold_time
            break
        hold_time += 1
    # Find last hold time to result in a win
    hold_time = race_time - 1
    while True:
        if hold_time * (race_time - hold_time) > record_distance:
            longest_hold_time = hold_time
            break
        hold_time -= 1
    # This is a parabola, all options between the first and the last result in a win
    ways_to_win = longest_hold_time - shortest_hold_time + 1
    print(f"{ways_to_win=}")

if __name__ == "__main__":
    main()
