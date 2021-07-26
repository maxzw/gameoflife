import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation as anim
from matplotlib import rc
rc('animation', html='jshtml')

# Run in Google Colab

class GameOfLife:
  
    def __init__(self, columns=10, rows=10, random=True):
        self.columns = columns
        self.rows = rows
        self.grid = self._make_grid(random=random)


    # helper function that generates the initial grid (empty or random)
    def _make_grid(self, random=False):
        new_grid = []
        for _ in range(0, self.rows):
            if random:
                new_grid.append(np.random.randint(2, size=self.columns).tolist())
            else:
                new_grid.append(np.zeros(self.columns).tolist())
        return new_grid

    
    # inserts glider gun at coordinate
    def insert_glidergun(self, coordinate: tuple):
        row, column = coordinate

        # first block
        self.grid[row+5][column+1] = 1
        self.grid[row+5][column+2] = 1
        self.grid[row+6][column+1] = 1
        self.grid[row+6][column+2] = 1

        # left object
        self.grid[row+3][column+14] = 1
        self.grid[row+3][column+13] = 1
        self.grid[row+4][column+12] = 1
        self.grid[row+5][column+11] = 1
        self.grid[row+6][column+11] = 1
        self.grid[row+7][column+11] = 1
        self.grid[row+8][column+12] = 1
        self.grid[row+9][column+13] = 1
        self.grid[row+9][column+14] = 1
        self.grid[row+6][column+15] = 1
        self.grid[row+4][column+16] = 1
        self.grid[row+8][column+16] = 1
        self.grid[row+5][column+17] = 1
        self.grid[row+6][column+17] = 1
        self.grid[row+7][column+17] = 1
        self.grid[row+6][column+18] = 1

        # right object
        self.grid[row+3][column+21] = 1
        self.grid[row+4][column+21] = 1
        self.grid[row+5][column+21] = 1
        self.grid[row+3][column+22] = 1
        self.grid[row+4][column+22] = 1
        self.grid[row+5][column+22] = 1
        self.grid[row+2][column+23] = 1
        self.grid[row+6][column+23] = 1
        self.grid[row+1][column+25] = 1
        self.grid[row+2][column+25] = 1
        self.grid[row+6][column+25] = 1
        self.grid[row+7][column+25] = 1

        # right block
        self.grid[row+3][column+35] = 1
        self.grid[row+4][column+35] = 1
        self.grid[row+3][column+36] = 1
        self.grid[row+4][column+36] = 1

    def _alive_dead_nb(self, row_idx, column_idx):
        
        '''
        Returns the amount of alive and dead neighbouring cells (total=8)
        '''

        alive = 0
        dead = 0

        for delta_row in [-1, 0, 1]:
            for delta_column in [-1, 0, 1]:
                if not (delta_row == 0 and delta_column == 0):
                    check_row_idx = row_idx + delta_row
                    check_column_idx = column_idx + delta_column
                    if (0 <= check_row_idx < self.rows) and (0 <= check_column_idx < self.columns):
                        if self.grid[check_row_idx][check_column_idx] == 1:
                            alive += 1
                        else:
                            dead += 1

        return alive, dead


    def _update_grid(self):
        
        '''
        Generates the grid at t+1 using rules and updates it
        '''  
        
        next_grid = self._make_grid()
        for row_idx, row in enumerate(self.grid):
            for column_idx, cell in enumerate(row):

                alive, dead = self._alive_dead_nb(row_idx, column_idx)

                if cell == 0 and alive == 3:
                    next_grid[row_idx][column_idx] = 1
                elif cell == 1 and alive == 2:
                    next_grid[row_idx][column_idx] = 1
                elif cell == 1 and alive == 3:
                    next_grid[row_idx][column_idx] = 1
                else:
                    next_grid[row_idx][column_idx] = 0

        self.grid = next_grid


    # helper function for animation
    def _animate(self, i):
        self.grid = self.im.get_array()
        self._update_grid()
        self.im.set_array(self.grid)
        return [self.im]


    # main function
    def run(self, frames, interval):
        fig = plt.figure(figsize=(8,8))
        plt.axis('off')
        self.im = plt.imshow(self.grid, cmap='gray_r', animated=True)
        plt.close(fig)
        self.animation = anim.FuncAnimation(fig, self._animate, frames=frames, interval=interval)


life = GameOfLife(rows=100, columns=100, random=True)
life.insert_glidergun((0,0))
life.run(frames=300, interval=100)
life.animation
