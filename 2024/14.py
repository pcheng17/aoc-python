import re
# import matplotlib.pyplot as plt
import numpy as np

def part_a(input):
    final = []
    nr = 103
    nc = 101
    for row in input.splitlines():
        nums = list(map(int, re.findall(r'-?\d+', row)))
        px, py, vx, vy = nums
        for _ in range(100):
            px = (px + vx) % nc
            py = (py + vy) % nr
        final.append((px, py))
    nwQuadrant = len([x for x in final if x[0] < nc//2 and x[1] < nr//2])
    neQuadrant = len([x for x in final if x[0] > nc//2 and x[1] < nr//2])
    swQuadrant = len([x for x in final if x[0] < nc//2 and x[1] > nr//2])
    seQuadrant = len([x for x in final if x[0] > nc//2 and x[1] > nr//2])

    return nwQuadrant * neQuadrant * swQuadrant * seQuadrant

def part_b(input):
    nr = 103
    nc = 101
    botp = []
    botv = []
    for row in input.splitlines():
        nums = list(map(int, re.findall(r'-?\d+', row)))
        px, py, vx, vy = nums
        botp.append((px, py))
        botv.append((vx, vy))

    eigenvalues = []
    for t in range(10403):
        for i in range(len(botp)):
            px, py = botp[i]
            vx, vy = botv[i]
            newx = (px + vx) % nc
            newy = (py + vy) % nr
            botp[i] = (newx, newy)

        possible = False
        for j in range(nr):
            tmp = list(sorted(set(x[0] for x in botp if x[1] == j)))
            if not tmp:
                continue
            curr = tmp[0]
            count = 1
            for k in range(1, len(tmp)):
                if tmp[k] == curr + 1:
                    count += 1
                else:
                    count = 1
                curr = tmp[k]
                if count == 8:
                    return t+1

        # if possible:
        #     # fig = plt.figure()
        #     grid = np.zeros((nr, nc))
        #     for x, y in botp:
        #         grid[y, x] = 1
        #     # plt.imshow(grid)
        #     # plt.show()
        #
        # points = np.array(botp)
        # mean = np.mean(points, axis=0)
        # points = points - mean
        # cov = np.cov(points.T)
        # evals, evecs = np.linalg.eig(cov)
        # eigenvalues.append((evals[0], evals[1]))

    # ers = [x[0]/x[1] for x in eigenvalues]
    # ts = list(range(10403))
    # plt.figure()
    # plt.scatter(ts, [x[0] for x in eigenvalues], label='eval1')
    # plt.scatter(ts, [x[1] for x in eigenvalues], label='eval2')
    # plt.scatter(ts[7752], eigenvalues[7752][0], color='red', marker='x')
    # plt.scatter(ts[7752], eigenvalues[7752][1], color='red', marker='x')
    # plt.legend()
    # plt.show()

