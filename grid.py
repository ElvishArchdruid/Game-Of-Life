import time


class Grid:
    def __init__(self, size : int):
        """
        Class for the grid of a game
        :param size: Integer n to define grid size as n*n
        """
        self.size = size
        self.grid_array = [['-' for i in range(size)] for j in range(size)]

    def display(self) -> None:
        """
        Prints the current grid state to the screen
        :return: None
        """

        for row in self.grid_array:
            print(row)

    def add_cell(self, x : int, y : int) -> None:
        """
        Method to add a living cell to the grid
        :param x: x coord of cell
        :param y: y coord of cell
        :return: None
        """

        self.grid_array[y][x] = '#'

    def get_neighbour_coords(self, x : int, y : int) -> list:
        """
        Method that gets the co-ordinates of each neighbouring cell in the grid
        :param x: X co-ordinate of the target cell
        :param y: Y co-ordinate of the target cell
        :return: A list of co-ordinates in the form [x, y]
        """
        neighbours_coords = []
        for row in range(-1,2):
            for col in range(-1,2):
                if row == col == 0:
                    pass
                elif x + row < 0 or x + row > self.size:
                    pass
                elif y + col < 0 or y + col > self.size:
                    pass
                else:
                    neighbours_coords.append([x+row, y+col])

        return neighbours_coords

    def get_state(self, x : int, y: int) -> bool:
        """
        Method that returns the state of a target cell
        :param x: X co-ordinate of the target cell
        :param y: Y co-ordinate of the target cell
        :return: True if alive, False if dead
        """
        if self.grid_array[y][x] == "#":
            return True
        else:
            return False

    def get_live_neighbours(self, x : int, y : int) -> int:
        """
        Method that returns the number of living neighbours a cell has
        :param x: X co-ordinate of the target cell
        :param y: Y co-ordinate of the target cell
        :return: Number of neighbours
        """
        count = 0
        for cell in self.get_neighbour_coords(x, y):
            if self.get_state(cell[1], cell[0]):
                count += 1

        return count

    def kill(self, x : int, y : int) -> None:
        """
        Method to turn live cells into dead cells
        :param x: X co-ordinate of the target cell
        :param y: Y co-ordinate of the target cell
        :return: None
        """
        self.grid_array[y][x] = "-"

    def birth(self, x : int, y : int) -> None:
        """
        Method to turn dead cells into live cells
        :param x: X co-ordinate of the target cell
        :param y: Y co-ordinate of the target cell
        :return: None
        """
        self.grid_array[y][x] = "#"

    def sim(self, gens : int) -> None:
        """
        Method to run the simulation for a number of generations
        :param gens: Number of generations to run the simulation for
        :return: None
        """
        for i in range(gens):
            print("= = = " * self.size)
            self.display()
            time.sleep(1)