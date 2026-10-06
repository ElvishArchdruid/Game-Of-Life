import pygame


BLACK = (0, 0, 0)


class Square:
    def __init__(self, x : int, y : int, size : int):
        """
        Class for each square in the visual grid
        :param x: X co-ordinate
        :param y: Y co-ordinate
        :pararm size: Square dimensions
        """
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x * size, y * size, size, size)
        self.state = False

    def draw(self, screen : pygame.Surface) -> None:
        """
        Draws the square to the screen 'alive'
        :param screen: Screen to draw to
        :return: None
        """
        if self.state:
            pygame.draw.rect(screen, BLACK, self.rect)
        else:
            pygame.draw.rect(screen, BLACK, self.rect, 1)

    def get_coords(self) -> list:
        return [self.x, self.y]

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_rect(self):
        return self.rect

    def live(self) -> None:
        self.state = True

    def die(self) -> None:
        self.state = False