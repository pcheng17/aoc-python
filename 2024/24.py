from graphviz import Digraph

def part_a(input):
    initial, wires_data = input.split('\n\n')
    vals = {}
    for line in initial.split('\n'):
        a, b = line.split(': ')
        vals[a] = int(b)

    wires = {}
    z = []
    for line in wires_data.split('\n'):
        lhs, rhs = line.split(' -> ')
        vars = lhs.split()
        wires[rhs] = (vars[0], vars[1], vars[2])
        if rhs.startswith('z'):
            z.append(rhs)

    z = sorted(z, reverse=True)

    while any(x not in vals for x in z):
        for lhs, expr in wires.items():
            try:
                match expr[1]:
                    case 'AND':
                        vals[lhs] = vals[expr[0]] & vals[expr[2]]
                    case 'OR':
                        vals[lhs] = vals[expr[0]] | vals[expr[2]]
                    case 'XOR':
                        vals[lhs] = vals[expr[0]] ^ vals[expr[2]]
            except:
                continue

    bitstr = ''.join(str(vals[x]) for x in z)
    return int(bitstr, 2)

def part_b(input):
    initial, wires_data = input.split('\n\n')
    vals = {}
    xs = []
    ys = []
    for line in initial.split('\n'):
        a, b = line.split(': ')
        vals[a] = int(b)
        if a.startswith('x'):
            xs.append(a)
        elif a.startswith('y'):
            ys.append(a)

    xs = sorted(xs, reverse=True)
    ys = sorted(ys, reverse=True)

    xarray = [vals[x] for x in xs]
    yarray = [vals[y] for y in ys]
    xbstr = ''.join(map(str, xarray))
    ybstr = ''.join(map(str, yarray))

    xpy = int(xbstr, 2) + int(ybstr, 2)
    xpybstr = f"{xpy:b}"

    # dot = Digraph()
    wires = {}
    zs = []
    for line in wires_data.split('\n'):
        lhs, rhs = line.split(' -> ')
        expr = lhs.split()
        wires[rhs] = (expr[0], expr[1], expr[2])
        # dot.edge(expr[0], rhs, label=expr[1])
        # dot.edge(expr[2], rhs, label=expr[1])
        if rhs.startswith('z'):
            zs.append(rhs)

    wires['kfp'], wires['hbs'] = wires['hbs'], wires['kfp']
    wires['z18'], wires['dhq'] = wires['dhq'], wires['z18']
    wires['z27'], wires['jcp'] = wires['jcp'], wires['z27']
    wires['pdg'], wires['z22'] = wires['z22'], wires['pdg']

    # dot.render('2024-24', format='png', cleanup=True)
    zs = sorted(zs, reverse=True)

    while any(x not in vals for x in zs):
        for lhs, expr in wires.items():
            try:
                match expr[1]:
                    case 'AND':
                        vals[lhs] = vals[expr[0]] & vals[expr[2]]
                    case 'OR':
                        vals[lhs] = vals[expr[0]] | vals[expr[2]]
                    case 'XOR':
                        vals[lhs] = vals[expr[0]] ^ vals[expr[2]]
            except:
                continue

    zbstr = ''.join(str(vals[x]) for x in zs)

    for i, (a, b) in enumerate(zip(xpybstr[::-1], zbstr[::-1])):
        if a != b:
            print(f"Bit {i} is different")

    ans = ['kfp', 'hbs', 'z18', 'dhq', 'z27', 'jcp', 'pdg', 'z22']
    return ','.join(sorted(ans))

