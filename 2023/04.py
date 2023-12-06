from collections import defaultdict

def part_a(input):
    data = input.splitlines()
    total = 0
    for line in data:
        a, b = line.split(':')
        winning_cards_str, my_cards_str = b.split('|')
        winning_cards = set(map(int, winning_cards_str.split()))
        my_cards = set(map(int, my_cards_str.split()))
        matches = my_cards.intersection(winning_cards)
        if matches:
            total += 2 ** (len(matches) - 1)
    return total

def part_b(input):
    data = input.splitlines()
    num_cards = len(data)
    cards = defaultdict(lambda: 0)
    for i, line in enumerate(data, 1):
        cards[i] += 1
        a, b = line.split(':')
        winning_cards_str, my_cards_str = b.split('|')
        winning_cards = set(map(int, winning_cards_str.split()))
        my_cards = set(map(int, my_cards_str.split()))
        matches = my_cards.intersection(winning_cards)
        for j in range(i + 1, min(i + len(matches) + 1, num_cards + 1)):
            cards[j] += cards[i]
    return sum(v for v in cards.values())
