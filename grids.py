import numpy as np

GRID_W = 5
GRID_H = 5
GRID = np.zeros((GRID_W, GRID_H))

ITER_W = range(GRID_W)
ITER_H = range(GRID_H)

for y in ITER_H:
    for x in ITER_W:
        GRID[y][x] = x + y if (y + x) % 2 == 0 else 0

G2 = np.zeros((GRID_W, GRID_H))

for y in ITER_H:
    for x in ITER_W:
        s = 0
        for j in range(-1, 2, 1):
            for i in range(-1, 2, 1):
                s += GRID[(y + j) % GRID_H][(x + i) % GRID_W]
        G2[y][x] = s

print(GRID)
print(G2)

np.array_repr
