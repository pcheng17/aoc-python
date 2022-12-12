from aocd import data
from typing import Callable
from tqdm import tqdm


GLOBALMOD = 1;

class FuncHandler:
    def __init__(self, expression: str, var: str) -> None:
        self.expression = expression
        self.var = var

    def __call__(self, x: int) -> int:
        return eval(self.expression, None, {self.var: x})


class Monkey:
    def __init__(self, 
                 items: list[int],
                 worryOp: FuncHandler,
                 testNums: tuple[int, int, int]) -> None:
        self.items = items
        self.worryOp = worryOp
        self.testNums = testNums
        self.inspCount = 0
        pass

    def size(self) -> int:
        return len(self.items)

    def processItemA(self, idx: int = 0) -> tuple[int, int]:
        self.inspCount += 1
        worryLvl = self.worryOp(self.items.pop(idx)) // 3
        dstMonkey = self.testNums[1] if (worryLvl % self.testNums[0]) == 0 else self.testNums[2]
        return worryLvl, dstMonkey

    def processItemB(self, idx: int = 0) -> tuple[int, int]:
        self.inspCount += 1
        worryLvl = self.worryOp(self.items.pop(idx)) % GLOBALMOD
        dstMonkey = self.testNums[1] if (worryLvl % self.testNums[0]) == 0 else self.testNums[2]
        return worryLvl, dstMonkey

    def addItem(self, item: int) -> None:
        self.items.append(item)

    def inspectionCount(self) -> int:
        return self.inspCount


def csvStrToIntList(csvStr: str):
    return list(map(int, csvStr.split(',')))


def parse(data):
    monkeys = []
    globalMod = 1
    monkeyData = data.split('\n\n')
    for info in monkeyData:
        infoList = info.split('\n')
        items = csvStrToIntList(infoList[1].split(':')[-1].strip()) 
        worryOpStr = infoList[2].split('=')[-1].strip()
        divBy = int(infoList[3].split('by')[-1].strip())
        globalMod *= divBy
        dstIfTrue = int(infoList[4].split()[-1].strip())
        dstIfFalse = int(infoList[5].split()[-1].strip())
        monkeys.append(Monkey(items, FuncHandler(worryOpStr, 'old'), (divBy, dstIfTrue, dstIfFalse)))
    return monkeys, globalMod


def partA(monkeys: list[Monkey]):
    for _ in range(20):
        for i in range(len(monkeys)):
            while monkeys[i].size() > 0:
                worry, dst = monkeys[i].processItemA()
                monkeys[dst].addItem(worry)

    inspCounts = [monkey.inspectionCount() for monkey in monkeys]
    inspCounts = sorted(inspCounts)
    return inspCounts[-1] * inspCounts[-2]


def partB(monkeys: list[Monkey]):
    for _ in tqdm(range(10000)):
        for i in range(len(monkeys)):
            while monkeys[i].size() > 0:
                worry, dst = monkeys[i].processItemB()
                monkeys[dst].addItem(worry)

    inspCounts = [monkey.inspectionCount() for monkey in monkeys]
    inspCounts = sorted(inspCounts)
    return inspCounts[-1] * inspCounts[-2]

        
monkeys, GLOBALMOD = parse(data)
print(f'Part A: {partA(monkeys)}')

monkeys, GLOBALMOD = parse(data)
print(f'Part B: {partB(monkeys)}')
