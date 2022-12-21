from aocd import data

monkeys = [x.replace(':', ' = ') for x in data.splitlines()]
while monkeys:
    for i, monkey in enumerate(monkeys):
        try:
            exec(monkey)
            del monkeys[i]
        except:
            pass

print(int(root))
