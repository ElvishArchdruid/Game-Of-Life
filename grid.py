class Grid:
    def __init__(self, size : int):
        """
        Class for the grid of a game
        :param size: Integer n to define grid size as n*n
        """
        self.size = size
        self.grid_array = [['0' for i in range(size)] for j in range(size)]

    def display(self) -> None:
        """
        Prints the current grid state to the screen
        :return: None
        """

        for row in self.grid_array:
            print(row)

    def add_cell(self, x : int, y : int) -> None:
        """
        Function to add a living cell to the grid
        :param x: x coord of cell
        :param y: y coord of cell
        :return: None
        """

        self.grid_array[y][x] = '#'