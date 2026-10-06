import sys
import pygame
import time

from square import Square
from grid import Grid


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (50, 200, 50)


class Game:
    def __init__(self, grid_size : int, square_size):
        """

        :param grid_size:
        :param square_size:
        """
        self.grid_size = grid_size
        self.square_size = square_size
        self.screen_size = grid_size * square_size
        self.grid = Grid(grid_size)

        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.SCREEN.fill(WHITE)

        self.squares = []
        self.init_grid()

        self.setup = True

    def main(self) -> None:
        """
        Main game loop
        :return: None
        """

        while True:
            self.SCREEN.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and self.setup:
                    pos = pygame.mouse.get_pos()

                    for s in self.squares:
                        if s.get_rect().collidepoint(pos):
                            if s.get_state():
                                s.kill()
                                self.grid.kill(s.get_x(), s.get_y())
                            else:
                                s.live()
                                self.grid.add_cell(s.get_x(), s.get_y())

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.setup = False
                        print("START")


            if not self.setup:
                self.update()
                time.sleep(1)

            self.draw()
            pygame.display.update()

    def init_grid(self) -> None:
        """
        Method to initialise the squares for the grid
        :return: None
        """
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                self.squares.append(Square(x, y, self.square_size))

    def draw(self) -> None:
        for s in self.squares:
            s.draw(self.SCREEN)

    def update(self):
        self.grid.update()

        for s in self.squares:
            if self.grid.get_state(s.get_x(), s.get_y()):
                s.live()
            else:
                s.kill()
