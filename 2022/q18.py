from aocd import data


test = '''
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
'''

DIRS = [
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, -1),
    (0, -1, 0),
    (-1, 0, 0),
]

def parse(data):
    voxels = set() 
    for line in data.splitlines():
        line = line.strip()
        if len(line) != 0:
            x, y, z = map(int, line.split(','))
            voxels.add((x, y, z))
    return voxels



def partA(input):
    surfaceArea = 0
    for voxel in input:
        count = 6
        for dir in DIRS:
            nbr = (voxel[0] + dir[0], voxel[1] + dir[1], voxel[2] + dir[2])
            if nbr in input:
                count -= 1
        surfaceArea += count
    return surfaceArea


def partB(input, solA):
    xs = [coord[0] for coord in input]
    ys = [coord[1] for coord in input]
    zs = [coord[2] for coord in input]
    xMin, xMax = min(xs)-1, max(xs)+1
    yMin, yMax = min(ys)-1, max(ys)+1
    zMin, zMax = min(zs)-1, max(zs)+1

    complement = set()

    for x in range(xMin, xMax+1):
        for y in range(yMin, yMax+1):
            for z in range(zMin, zMax+1):
                voxel = (x, y, z)
                if voxel not in input:
                    complement.add(voxel)

    queue = set([(xMin, yMin, zMin)])

    while len(queue):
        tmp = set()
        for voxel in queue:
            for dir in DIRS:
                nbr = (voxel[0] + dir[0], voxel[1] + dir[1], voxel[2] + dir[2])
                if nbr in complement:
                    tmp.add(nbr)
            complement.remove(voxel)
        queue = tmp

    saBubbles = partA(complement)
    return solA - saBubbles


def solveA(input):
    return partA(input)


def solveB(input):
    return partB(input, partA(input))


if __name__ == '__main__':
    input = parse(data)
    print(f'Part A: {solveA(input)}')
    print(f'Part B: {solveB(input)}')
