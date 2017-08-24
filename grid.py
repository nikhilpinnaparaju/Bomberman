import os
import random

score = 0

lines = 19
columns = 19

grid = []

for row in range(lines):
    grid.append([])

    for col in range(columns):
        if (row == 0) or (col == 0) or (row == lines - 1) or (col == columns - 1):
            grid[row].append('X')

        elif row % 2:
            grid[row].append(' ')

        elif not(col % 2):
            grid[row].append('X')

        else:
            grid[row].append(' ')

for i in range(25):
    x = random.randrange(lines)
    y = random.randrange(columns)

    while grid[x][y] != ' ':
        x = random.randrange(lines)
        y = random.randrange(columns)

    grid[x][y] = '/'

# def print_board(grid):
#     os.system('clear')
#     for row in grid:
# 		# for ch in row:


def convert(grid):
    output = [[" " for i in range(4 * columns)] for j in range(2 * lines)]
    for i in range(len(grid)):
        for j in range(len(grid)):
            output[2 * j][4 * i] = grid[i][j]
            output[2 * j][4 * i + 1] = grid[i][j]
            output[2 * j][4 * i + 2] = grid[i][j]
            output[2 * j][4 * i + 3] = grid[i][j]
            output[2 * j + 1][4 * i] = grid[i][j]
            output[2 * j + 1][4 * i + 1] = grid[i][j]
            output[2 * j + 1][4 * i + 2] = grid[i][j]
            output[2 * j + 1][4 * i + 3] = grid[i][j]

    return output


def print_board(grid):
    output = convert(grid)

    os.system('clear')
    for row in output:
        print("".join(row), '\n', end='\r')
    print("Lives: ", 3, " Score:", score, end='\r')
    print("\n")
