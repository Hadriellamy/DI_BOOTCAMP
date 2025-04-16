#Instructions
"""
These are the rules of the Game of Life (as stated in Wikipedia):

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively).

Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
Using these rules, implement the Game. (Hint: use Classes !!!!)
Use a few different initial states to see how the game ends.

Notes:

Display the grid after each generation
The end of the game is fully determined by the initial state. So have it pass through your program and see how it ends.
Be creative, but use classes
The game can have fixed borders and can also have moving borders. First implement the fixed borders. Each “live” cell that is going out of the border, exits the game.
Bonus: Make the game with ever expandable borders, make the maximum border size a very large number(10,000) so you won’t cause a memory overflow

"""

import time
import os
import copy

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        self.grid = self.create_grid(False)

        if initial_state:
            for r, c in initial_state:
                if 0 <= r < rows and 0 <= c < cols:
                    self.grid[r][c] = True

    def create_grid(self, default=False):
        return [[default for _ in range(self.cols)] for _ in range(self.rows)]

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")
        for row in self.grid:
            print("".join("⬛" if cell else "⬜" for cell in row))
        print("\n")

    def count_live_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.grid[r][c]:
                    count += 1
        return count

    def next_generation(self):
        new_grid = self.create_grid()
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_live_neighbors(r, c)
                if self.grid[r][c]:
                    new_grid[r][c] = live_neighbors in [2, 3]
                else:
                    new_grid[r][c] = live_neighbors == 3
        self.grid = new_grid

    def run(self, generations=10, delay=0.5):
        for gen in range(generations):
            print(f"Generation {gen + 1}")
            self.display()
            self.next_generation()
            time.sleep(delay)

#Test
if __name__ == "__main__":
    glider = [
        (1, 2),
        (2, 3),
        (3, 1), (3, 2), (3, 3)
    ]

    game = GameOfLife(rows=10, cols=10, initial_state=glider)
    game.run(generations=20, delay=0.3)
