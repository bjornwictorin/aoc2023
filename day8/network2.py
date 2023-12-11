#!/usr/bin/env python3

from re import search
from typing import List

def prime_factors(val: int) -> List[int]:
    factors = []
    for ii in range(2, val//2):
        if val % ii == 0:
            factors.append(ii)
    if len(factors) > 0:
        print(f"{val} is not prime, because it is a multiple of {[ii for ii in factors]}")
    # If no divisor is found, the number is its own only divisor
    if len(factors) == 0:
        factors.append(val)
    return factors

def main():
    directions = ""
    node_map = {}
    with open("input.txt", "r") as f:
        first_line = True
        pattern = r"(.*) = \((.*), (.*)\)"
        for line in f:
            if first_line:
                directions = line.strip()
                first_line = False
            elif len(line) != 1:
                match = search(pattern, line)
                node_map[match.group(1)] = (match.group(2), match.group(3))
    # Find all starting points
    start_positions = [node for node in node_map.keys() if node[2] == "A"]
    steps_on_z = []
    print(start_positions)
    for ii, start_pos in enumerate(start_positions):
        total_steps = 0
        pos = start_pos
        last_hit = 0
        first_diff = True
        while total_steps < 100000:
            dir = directions[total_steps % len(directions)]
            pos = node_map[pos][0] if dir == "L" else node_map[pos][1]
            total_steps += 1
            if pos[2] == "Z":
                print(f"{total_steps - last_hit}, ", end="")
                if first_diff:
                    steps_on_z.append(total_steps - last_hit)
                first_diff = False
                last_hit = total_steps
        print()
    print(f"{steps_on_z=}")
    # Find prime factors and calculate GCD
    all_prime_factors = set()
    for step in steps_on_z:
        # print(prime_factors(step))
        all_prime_factors.update(prime_factors(step))

    gcd = 1
    for factor in all_prime_factors:
        gcd *= factor

    print(f"{gcd=}")

if __name__ == "__main__":
    main()
