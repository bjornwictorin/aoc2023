#!/usr/bin/env python3


def main():
    ways_to_win_product = 1
    times = [48, 93, 85, 95]
    distances = [296, 1928, 1236, 1391]
    for race_time, record_distance in zip(times, distances):
        ways_to_win = 0
        for hold_time in range(1, race_time):
            if hold_time * (race_time - hold_time) > record_distance:
                ways_to_win += 1
        ways_to_win_product *= ways_to_win
    print(f"{ways_to_win_product=}")

if __name__ == "__main__":
    main()
