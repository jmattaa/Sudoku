from copy import deepcopy
import pygame as p
import random

class Sudoku:
    def __init__(self, r_w, r_h):
        """Create a sudoku class

        Args:
            r_w (int): The width of each square/cell in the grid
            r_h (int): The height of each square/cell in the grid
        """
        self.r_w = r_w
        self.r_h = r_h

        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0,],
        ]

        self.initialGrid = []
        self.solvedState = []
        self.win = False

        self.generateGrid()

    def generateGrid(self):
        base = 3
        side = base * base

        def pattern(r, c):
            return (base * (r % base) + r // base + c) % side

        # randomize rows, columns and numbers (of valid base pattern)
        def shuffle(s):
            return random.sample(s, len(s))

        rBase = range(base)
        rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, side + 1))

        self.grid = [[nums[pattern(r, c)] for c in cols] for r in rows]
        self.solvedState = deepcopy(self.grid)

        squares = side * side
        empties = random.randint(
            12, 81 - 17
        )  # 17 is the least amount of numbers for sudoku 12 is arbitrary
        for s in random.sample(range(squares), empties):
            self.grid[s // side][s % side] = 0

        self.initialGrid = deepcopy(self.grid)

    def highlight(self, screen, pos):
        """Highlight a square/cell in the grid

        Args:
            screen (pygame screen): The screen to draw on
            pos (int): The position of the square/cell to highlight
        """
        i, j = pos
        p.draw.rect(
            screen,
            p.Color(0, 140, 255),
            p.Rect(i * self.r_w, j * self.r_h, self.r_w, self.r_h),
            4,
        )

    def addNumber(self, pos, n):
        """add a number to the grid

        Args:
            pos (tuple(x, y)): the position where the number should be placed
            n (_type_): the number to be placed
        """
        # y and x are inverted for some reason
        x, y = pos
        if self.initialGrid[y][x] != 0:
            return

        self.grid[y][x] = n

        if self.grid == self.solvedState: self.win = True

    def draw(self, screen, font1, font2):
        """Draws the sudoku board.

        Args:
            screen (pygame screen): the screen to draw the board on.
            font1 (pygame font): the font to draw the on the board for the numbers that are initially made.
            font2 (pygame font): the font used to draw the numbers user placed
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    continue

                text = font1.render(str(self.grid[i][j]), 1, (0, 0, 0))
                if self.grid[i][j] != self.initialGrid[i][j]:
                    text = font2.render(str(self.grid[i][j]), 1, (0, 128, 255))

                screen.blit(
                    text, (self.r_w * j + (self.r_w / 3), self.r_h * i + (self.r_h / 4))
                )

        for i in range(10):
            if i % 3 == 0:
                thick = 3
            else:
                thick = 1

            p.draw.line(
                screen,
                (0, 0, 0),
                (0, i * self.r_w),
                (screen.get_width(), i * self.r_w),
                thick,
            )
            p.draw.line(
                screen,
                (0, 0, 0),
                (i * self.r_h, 0),
                (i * self.r_h, screen.get_height()),
                thick,
            )
