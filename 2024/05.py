from functools import cmp_to_key

def check(rules, update):
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        i = update.index(rule[0])
        j = update.index(rule[1])
        if i > j:
            return False
    return True

def parse(input):
    sec0, sec1 = input.split("\n\n")
    rules = []
    for rule in sec0.splitlines():
        a, b = rule.split("|")
        rules.append((int(a), int(b)))

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

    def cmp(a, b):
        for row in rules:
            if row[0] == a and row[1] == b:
                return -1
            elif row[0] == b and row[1] == a:
                return 1
            else:
                continue

    total = 0
    for row in asdf:
        row.sort(key=cmp_to_key(cmp))
        total = total + row[len(row) // 2]
    return total




