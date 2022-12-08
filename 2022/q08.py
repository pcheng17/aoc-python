from aocd import data

test = '''30373
25512
65332
33549
35390'''


def parse(data):
    lines = data.splitlines()
    trees = []
    for line in lines:
        trees.append([int(c) for c in line])
    return trees

def partA(treeGrid):
    rows = len(treeGrid)
    cols = len(treeGrid[0])

    canSee = [[False for _ in range(cols)] for _ in range(rows)]

    for j in range(cols):
        canSee[0][j] = True
        canSee[-1][j] = True

    for i in range(rows):
        canSee[i][0] = True
        canSee[i][-1] = True

    for i in range(1, rows-1):
        height = treeGrid[i][0]
        for j in range(1, cols-1):
            if treeGrid[i][j] > height:
                canSee[i][j] = True
                height = treeGrid[i][j]

        height = treeGrid[i][-1]
        for j in reversed(range(1, cols-1)):
            if treeGrid[i][j] > height:
                canSee[i][j] = True
                height = treeGrid[i][j]

    for j in range(1, cols-1):
        height = treeGrid[0][j]
        for i in range(1, rows-1):
            if treeGrid[i][j] > height:
                canSee[i][j] = True
                height = treeGrid[i][j]

        height = treeGrid[-1][j]
        for i in reversed(range(1, rows-1)):
            if treeGrid[i][j] > height:
                canSee[i][j] = True
                height = treeGrid[i][j]

    return sum(row.count(True) for row in canSee)
      


def partB(treeGrid):
    rows = len(treeGrid)
    cols = len(treeGrid[0])

    score = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            upScore = 0
            downScore = 0
            leftScore = 0
            rightScore = 0
            
            ii = i-1
            while ii >= 0:
                upScore += 1
                if treeGrid[ii][j] < treeGrid[i][j]:
                    ii -= 1
                else:
                    break

            ii = i+1
            while ii < rows:
                downScore += 1
                if treeGrid[ii][j] < treeGrid[i][j]:
                    ii += 1
                else:
                    break

            jj = j-1
            while jj >= 0:
                leftScore += 1
                if treeGrid[i][jj] < treeGrid[i][j]:
                    jj -= 1
                else: 
                    break

            jj = j+1
            while jj < cols:
                rightScore += 1
                if treeGrid[i][jj] < treeGrid[i][j]:
                    jj += 1
                else: 
                    break

            score[i][j] = upScore * downScore * leftScore * rightScore;
    return max([max(row) for row in score])


treeGrid = parse(data)
print(f'Part A: {partA(treeGrid)}')
print(f'Part B: {partB(treeGrid)}')
