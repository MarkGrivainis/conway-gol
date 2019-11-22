from functools import wraps
import numpy as np
from numba import jit
from numba import prange
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Constants
# ========
FPS = 60
GRID_W = 150
GRID_H = 150
# ========





def timefn(fn):
    """wrapper to time the enclosed function"""

    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print("@timefn: {} took {} seconds".format(fn.__name__, t2 - t1))
        return result

    return measure_time


def initialize_grid(width=20, height=20, config=None, x=0, y=0):
    """Function to generate t=0 grid.
    Currently this function has two builtin configurations:
        r-pentamino
        glider

    :param N: The width of the grid
    :param config: which configuration to choose
    :param x: The x offset for the initial configuration
    :param y: The y offset for the initial configuration
    :returns grid: Initialized 2D numpy grid

    """
    grid = np.zeros((width, height))
    if config == "glider":
        grid[0][1] = 1
        grid[1][2] = 1
        grid[2][0] = 1
        grid[2][1] = 1
        grid[2][2] = 1
    elif config == "pentamino":
        grid[y + 0][x + 1] = 1
        grid[y + 0][x + 2] = 1
        grid[y + 1][x + 0] = 1
        grid[y + 1][x + 1] = 1
        grid[y + 2][x + 1] = 1
    return grid


# @jit(parallel=True, nopython=True, fastmath=True)
# @jit
def update_grid(grid):
    g_len = grid.shape[0]
    grid_new = np.zeros(grid.shape)
    for y in prange(g_len):
        for x in range(g_len):
            total = 0
            for j in range(-1, 2, 1):
                for i in range(-1, 2, 1):
                    total += grid[(y + j) % g_len][(x + i) % g_len]
            total -= grid[y][x]
            alive = grid[y][x] > 0
            if alive and total < 2:
                grid_new[y][x] = 0
            elif alive and 2 <= total <= 3:
                grid_new[y][x] = 1
            elif alive and 3 < total:
                grid_new[y][x] = 0
            elif not alive and total == 3:
                grid_new[y][x] = 1
    return grid_new


def update(frame, im, grid):
    new_grid = update_grid(grid)
    im.set_array(new_grid)
    grid[:] = new_grid[:]
    return (im,)


@timefn
def draw_N(grid, N):
    for i in range(N):
        grid[:] = update_grid(grid)[:]


@timefn
def main():
    grid = initialize_grid(width=GRID_W, height=GRID_H, config="pentamino", x=75, y=75)
    # draw_N(grid, 1000)
    # update_grid.parallel_diagnostics(level=1)
    fig = plt.figure()
    im = plt.imshow(
        grid, cmap="Greys", aspect="equal", interpolation="none", vmin=0, vmax=1
    )
    ani = FuncAnimation(
        fig,
        update,
        fargs=(im, grid),
        frames=FPS * 50,
        interval=1000 / FPS,
        repeat=False,
    )
    plt.show()
    return ani


if __name__ == "__main__":
    ani = main()
    # ani.save("./test.mpg")
