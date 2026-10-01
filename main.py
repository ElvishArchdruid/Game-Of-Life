from grid import Grid

grid = Grid(5)
grid.add_cell(1,2)
print(grid.get_live_neighbours(1,1))
grid.display()