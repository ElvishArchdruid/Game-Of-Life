import sys
import pygame
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
            self.draw_grid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


    def draw_grid(self) -> None:
        """
        Method to draw the grid to the screen
        :return: None
        """
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)
                pygame.draw.rect(self.SCREEN, BLACK, rect)
