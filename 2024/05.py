from collections import defaultdict

def check(rules, update):
    for i in range(1, len(update)):
        if update[i] in rules:
            if update[i-1] in rules[update[i]]:
                return False
    return True

def parse(input):
    sec0, sec1 = input.split("\n\n")
    rules = defaultdict(set)
    for rule in sec0.splitlines():
        a, b = rule.split("|")
        rules[int(a)].add(int(b))

    updates = []
    for row in sec1.splitlines():
        updates.append(list(map(int, row.split(','))))

    return rules, updates

def part_a(input):
    rules, updates = parse(input)

    total = 0
    for row in updates:
        if check(rules, row):
            total = total + row[len(row) // 2]

    return total

def part_b(input):
    rules, updates = parse(input)

    asdf = []
    for row in updates:
        if not check(rules, row):
            asdf.append(row)

    def bubblesort(arr):
        for i in range(len(arr)):
            swapped = False
            for j in range(0, len(arr)-i-1):
                if arr[j+1] in rules and arr[j] in rules[arr[j+1]]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True

            if not swapped:
                break

        return arr

    total = 0
    for row in asdf:
        row = bubblesort(row)
        total = total + row[len(row) // 2]
    return total

