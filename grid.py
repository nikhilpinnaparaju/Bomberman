lines = 19
columns = 19

grid = []

for row in range(lines):
    grid.append([])

    for col in range(columns):
        if (row==0) or (col==0) or (row==lines-1) or (col==columns-1):
             grid[row].append('X')

        elif row%2:
            grid[row].append(' ')

        elif not(col%2):
            grid[row].append('X')

        else:
            grid[row].append(' ')

def print_board(grid):
	for row in grid:
		# for ch in row:
            print("".join(row))

# print(grid)
# print_board(grid)