#!/usr/bin/env python3

from enum import Enum
from typing import Tuple, Literal

class HandType(Enum):
    five_of_a_kind = 6
    four_of_a_kind = 5
    full_house = 4
    three_of_a_kind = 3
    two_pair = 2
    one_pair = 1
    high_card = 0


def get_hand_type(hand: Tuple[str, int]) -> Literal[6, 5, 4, 3, 2, 1, 0]:
    assert len(hand[0]) == 5, hand
    occurences = {}
    for char in hand[0]:
        if char not in occurences:
            occurences[char] = 1
        else:
            occurences[char] += 1
    assert sum(occurences.values()) == 5
    card_dist = sorted(occurences.values())
    hand_type = HandType.high_card
    if card_dist == [5]:
        hand_type = HandType.five_of_a_kind
    elif card_dist == [1, 4]:
        hand_type = HandType.four_of_a_kind
    elif card_dist == [2, 3]:
        hand_type = HandType.full_house
    elif card_dist == [1, 1, 3]:
        hand_type = HandType.three_of_a_kind
    elif card_dist == [1, 2, 2]:
        hand_type = HandType.two_pair
    elif card_dist == [1, 1, 1, 2]:
        hand_type = HandType.one_pair
    elif card_dist == [1, 1, 1, 1, 1]:
        hand_type = HandType.high_card
    else:
        assert False
    return hand_type.value


def get_card_rank(card: str, index: int) -> int:
    valid_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    assert 0 <= index < 5
    assert card[index] in valid_cards
    return valid_cards.index(card[index])


def main():
    total_winning = 0
    hands = []
    with open("input.txt", "r") as f:
        for line in f:
            hand, bid = line.strip().split(" ")
            hands.append((hand, int(bid)))

    for ii in reversed(range(5)):
        hands.sort(key=lambda x: get_card_rank(x[0], ii))
    hands.sort(key=get_hand_type)
    for ii, hand in enumerate(hands):
        _, bid = hand
        total_winning += (ii + 1) * bid
    print(f"{total_winning=}")

if __name__ == "__main__":
    main()
