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

    def bubblesort(arr):
        for i in range(len(arr)):
            swapped = False
            for j in range(0, len(arr)-i-1):
                for r in rules:
                    if r[0] == arr[j+1] and r[1] == arr[j]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        swapped = True
                        break

            if not swapped:
                break

        return arr

    total = 0
    for row in asdf:
        row = bubblesort(row)
        total = total + row[len(row) // 2]
    return total

