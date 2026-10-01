import sys
import pygame
import time

import grid
from grid import Grid


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

class Game:
    def __init__(self, grid_size : int, block_size):
        self.grid_size = grid_size
        self.block_size = block_size
        self.screen_size = grid_size * block_size
        self.grid = Grid(grid_size)

        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.SCREEN.fill(WHITE)

    def main(self) -> None:
        """
        Main game loop
        :return: None
        """

        while True:
            self.SCREEN.fill(WHITE)
            self.draw_grid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

            time.sleep(1)
            self.grid.update()


    def set_grid(self):
        self.grid.add_cell(7, 7)
        self.grid.add_cell(7, 8)
        self.grid.add_cell(6, 8)
        self.grid.add_cell(8, 8)


    def draw_grid(self) -> None:
        """
        Method to draw the grid to the screen
        :return: None
        """
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid.get_array()[y][x] == "#":
                    rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)
                    pygame.draw.rect(self.SCREEN, BLACK, rect)
