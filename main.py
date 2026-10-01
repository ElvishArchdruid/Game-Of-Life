from grid import Grid

grid = Grid(9)
grid.add_cell(4,3)
grid.add_cell(4, 4)
grid.add_cell(3,4)
grid.add_cell(5,4)
grid.sim(20)