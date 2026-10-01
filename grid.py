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
        :param y: Y co-ordinate of the target cekk
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