import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation as anim
from matplotlib import rc
rc('animation', html='jshtml')

columns = 100
rows = 100

fig = plt.figure()
plt.axis('off')


# making grid
def make_grid(n_rows, n_columns, random=False):
    new_grid = []
    for _ in range(0, n_rows):
        if random:
            new_grid.append(np.random.randint(2, size=n_columns).tolist())
        else:
            new_grid.append(np.zeros(n_columns).tolist())
    return new_grid


def alive_dead_nb(grid, row_idx, column_idx):
    global rows, columns

    alive = 0
    dead = 0

    for delta_row in [-1, 0, 1]:
        for delta_column in [-1, 0, 1]:
            if not (delta_row == 0 and delta_column == 0):
                check_row_idx = row_idx + delta_row
                check_column_idx = column_idx + delta_column
                if (0 <= check_row_idx < rows) and (0 <= check_column_idx < columns):
                    if grid[check_row_idx][check_column_idx] == 1:
                        alive += 1
                    else:
                        dead += 1

    return alive, dead


grid = make_grid(rows, columns, random=True)
im = plt.imshow(grid, cmap='gray_r', animated=True)

def update_grid():
    global grid

    next_grid = make_grid(rows, columns)

    for row_idx, row in enumerate(grid):
        for column_idx, cell in enumerate(row):

            alive, dead = alive_dead_nb(grid, row_idx, column_idx)

            # print('Cell {0},{1} with {2} alive and {3} dead'.format(row_idx, column_idx, alive, dead))

            if cell == 0 and alive == 3:
                next_grid[row_idx][column_idx] = 1
            elif cell == 1 and alive == 2:
                next_grid[row_idx][column_idx] = 1
            elif cell == 1 and alive == 3:
                next_grid[row_idx][column_idx] = 1
            else:
                next_grid[row_idx][column_idx] = 0

    grid = next_grid


def animate(self):
    global grid
    grid = im.get_array()
    update_grid()
    im.set_array(grid)
    return [im]


anim = anim.FuncAnimation(fig, animate, frames=200, interval=250, blit=True)
anim