from collections import Counter
import sys

def adjust_card_values(hand, is_part2):
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('2') - 1) if is_part2 else chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))
    return hand

def evaluate_hand(hand, is_part2):
    hand = adjust_card_values(hand, is_part2)
    card_counts = Counter(hand)

    if is_part2:
        target = list(card_counts.keys())[0]
        for card in card_counts:
            if card != '1':
                if card_counts[card] > card_counts[target] or target == '1':
                    target = card
        assert target != '1' or list(card_counts.keys()) == ['1']
        if '1' in card_counts and target != '1':
            card_counts[target] += card_counts['1']
            del card_counts['1']
        assert '1' not in card_counts or list(card_counts.keys()) == ['1'], f'{card_counts} {hand}'

    sorted_card_values = sorted(card_counts.values())

    if sorted_card_values == [5]:
        return (10, hand)
    elif sorted_card_values == [1, 4]:
        return (9, hand)
    elif sorted_card_values == [2, 3]:
        return (8, hand)
    elif sorted_card_values == [1, 1, 3]:
        return (7, hand)
    elif sorted_card_values == [1, 2, 2]:
        return (6, hand)
    elif sorted_card_values == [1, 1, 1, 2]:
        return (5, hand)
    elif sorted_card_values == [1, 1, 1, 1, 1]:
        return (4, hand)
    else:
        assert False, f'{card_counts} {hand} {sorted_card_values}'

def main(file_path):
    data = open(file_path).read().strip()
    lines = data.split('\n')

    hands_and_bids = []
    for line in lines:
        hand, bid = line.split()
        hands_and_bids.append((hand, bid))

    for is_part2 in [False, True]:
        hands_and_bids = sorted(hands_and_bids, key=lambda hb: evaluate_hand(hb[0], is_part2))
        total_score = sum((i + 1) * int(bid) for i, (hand, bid) in enumerate(hands_and_bids))
        print(total_score)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
    else:
        main(sys.argv[1])
