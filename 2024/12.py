from collections import defaultdict

def conncomp(coords):
    components = []
    visited = set()

    def get_neighbors(i, j):
        possible = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        return [p for p in possible if p in coords]

    def dfs(coord):
        component = set()
        stack = [coord]

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component.add(current)
                i, j = current
                neighbors = get_neighbors(i, j)
                stack.extend(neighbors)

        return component

    for coord in coords:
        if coord not in visited:
            component = dfs(coord)
            components.append(component)

    return components

def get_number_of_sides(coords):
    def get_neighbor_mask(i, j):
        nbrs = {
            "NW": (i-1, j-1),
            "N": (i-1, j),
            "NE": (i-1, j+1),
            "W": (i, j-1),
            "E": (i, j+1),
            "SW": (i+1, j-1),
            "S": (i+1, j),
            "SE": (i+1,j+1)
        }
        return {k: v for k, v in nbrs.items() if v in coords}

    visited = set()
    corners = 0

    for coord in coords:
        i, j = coord
        neighbors = get_neighbor_mask(i, j)
        for d1 in ["N", "S"]:
            for d2 in ["W", "E"]:
                if d1 in [x for x in neighbors.keys()]:
                    if d2 in [x for x in neighbors.keys()]:
                        if f"{d1}{d2}" not in neighbors:
                            if frozenset([coord, neighbors[d1], neighbors[d2]]) not in visited:
                                visited.add(frozenset([coord, neighbors[d1], neighbors[d2]]))
                                corners += 1
                    else:
                        if f"{d1}{d2}" in neighbors:
                            if frozenset([coord, neighbors[d1], neighbors[f"{d1}{d2}"]]) not in visited:
                                visited.add(frozenset([coord, neighbors[d1], neighbors[f"{d1}{d2}"]]))
                                corners += 1
                else:
                    if d2 in neighbors:
                        if f"{d1}{d2}" in neighbors:
                            if frozenset([coord, neighbors[d2], neighbors[f"{d1}{d2}"]]) not in visited:
                                visited.add(frozenset([coord, neighbors[d2], neighbors[f"{d1}{d2}"]]))
                                corners += 1
                    else:
                        if f"{d1}{d2}" in neighbors:
                            if frozenset([coord, neighbors[f"{d1}{d2}"]]) not in visited:
                                visited.add(frozenset([coord, neighbors[f"{d1}{d2}"]]))
                                corners += 2
                        else:
                            corners += 1

    return corners

def part_a(input):
    data = input.splitlines()
    groups = defaultdict(list)
    for i, row in enumerate(data):
        for j, x in enumerate(row):
            groups[x].append((i, j))

    total = 0
    for _, coords in groups.items():
        cc = conncomp(coords)
        for component in cc:
            area = len(component)
            perimeter = 0
            for coord in component:
                i, j = coord
                neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                perimeter += sum(1 for n in neighbors if n not in component)
            total += area * perimeter
    return total


def part_b(input):
    data = input.splitlines()
    groups = defaultdict(list)
    for i, row in enumerate(data):
        for j, x in enumerate(row):
            groups[x].append((i, j))

    total = 0
    for f, coords in groups.items():
        cc = conncomp(coords)
        for component in cc:
            area = len(component)
            num_sides = get_number_of_sides(component)
            total += area * num_sides
    return total
