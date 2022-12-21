from aocd import data
from copy import deepcopy
import sympy as sp



test = '''
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
'''

VAR = 'humn'

def parse(data):
    variables = {}
    expressions = {}
    for line in data.strip().splitlines():
        lhs, rhs = line.split(':')
        if rhs.strip().isnumeric():
            variables[lhs] = str(rhs.strip())
        else:
            expressions[lhs] = str(rhs.strip())
    return (variables, expressions)


def partA(variables, expressions):
    while expressions:
        for k, v in variables.items():
            for x, y in expressions.items():
                if k in y:
                    tmp = y.replace(k, str(v))
                    expressions[x] = tmp

        to_del = []
        for x, y in expressions.items():
            if not any(c.isalpha() for c in y):
                variables[x] = eval(y)
                to_del.append(x)

        for x in to_del:
            del expressions[x]

    return variables['root']


def partB(variables, expressions):
    # First modify the input for this problem
    del variables[VAR]
    rootLeft, _, rootRight = expressions['root'].split(' ')
    del expressions['root']

    numExpressions = len(expressions)

    while expressions:
        # Substitute variables
        for k, v in variables.items():
            for x, y in expressions.items():
                if k in y:
                    tmp = y.replace(k, str(v))
                    expressions[x] = tmp

        to_del = []
        for x, y in expressions.items():
            if not any(c.isalpha() for c in y):
                variables[x] = eval(y)
                to_del.append(x)

        for x in to_del:
            del expressions[x]

        # If number of expressions didn't change, that means we're done substituting
        if numExpressions == len(expressions):
            break
        else:
            numExpressions = len(expressions)

    # Brute force plug expressions into each other
    for k, v in expressions.items():
        for x, y in expressions.items():
            if k in y:
                tmp = y.replace(k, f'({v})')
                expressions[x] = tmp

    # Make final substitution into the LHS of root's expression
    if rootLeft in variables:
        rootLeft = str(variables[rootLeft])
    else:
        rootLeft = f'({expressions[rootLeft]})'

    # Make final substitution into the RHS of root's expression
    if rootRight in variables:
        rootRight = str(variables[rootRight])
    else:
        rootRight = f'({expressions[rootRight]})'

    rootLeft = rootLeft.replace(VAR, 'x')
    rootRight = rootRight.replace(VAR, 'x')

    x, y = sp.symbols('x y')
    equation = sp.Eq(y, eval(f'{rootRight} - {rootLeft}'))
    return sp.solve(equation.subs(y, 0))[0]
      

def solveA(input):
    vars, exprs = deepcopy(input)
    return partA(vars, exprs)


def solveB(input):
    vars, exprs = deepcopy(input)
    return partB(vars, exprs)


if __name__ == '__main__':
    input = parse(test)
    print(f'Part A: {solveA(input)}')

    input = parse(data)
    print(f'Part B: {solveB(input)}')
