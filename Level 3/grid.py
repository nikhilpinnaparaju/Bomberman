import os
import random
from termcolor import colored, cprint
# from colored import fore, style

score = 0

# declaration of the number of rows and columns that will be in our grid
lines = 15
columns = 15

grid = []

# The following for loops make the board to a design that we would want as soon from the sample in the Problem statement
# The grid at the moment is in 1*1 elements and later we will convert each element into 2*4 elements
for row in range(lines):
    grid.append([])

    for col in range(columns):
        if ((row == 0) or (col == 0) or (row == lines - 1) or
                (col == columns - 1)):
            grid[row].append('X')

        elif row % 2:
            grid[row].append(' ')

        elif not(col % 2):
            grid[row].append('X')

        else:
            grid[row].append(' ')

# Randomly generated bricks that can be destroyed by our bomberman's bomb
for i in range(25):
    x = random.randrange(3, lines)
    y = random.randrange(3, columns)

    while grid[x][y] != ' ':
        x = random.randrange(3, lines)
        y = random.randrange(3, columns)

    grid[x][y] = '/'

# def print_board(grid):
#     os.system('clear')
#     for row in grid:
# 		# for ch in row:

# the convert function changes our 1*1 elements into elements each of size 2*4
def convert(grid):
    output = [[" " for i in range(4 * columns)] for j in range(2 * lines)]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (grid[i][j] == '3' or grid[i][j] == '2' or grid[i][j] == '1' or grid[i][j] == '0' or grid[i][j] == '4' or grid[i][j] == '5'):
                output[2 * j][4 * i] = '['
                output[2 * j][4 * i + 1] = grid[i][j]
                output[2 * j][4 * i + 2] = grid[i][j]
                output[2 * j][4 * i + 3] = ']'
                output[2 * j + 1][4 * i] = '['
                output[2 * j + 1][4 * i + 1] = grid[i][j]
                output[2 * j + 1][4 * i + 2] = grid[i][j]
                output[2 * j + 1][4 * i + 3] = ']'

            else:
                output[2 * j][4 * i] = grid[i][j]
                output[2 * j][4 * i + 1] = grid[i][j]
                output[2 * j][4 * i + 2] = grid[i][j]
                output[2 * j][4 * i + 3] = grid[i][j]
                output[2 * j + 1][4 * i] = grid[i][j]
                output[2 * j + 1][4 * i + 1] = grid[i][j]
                output[2 * j + 1][4 * i + 2] = grid[i][j]
                output[2 * j + 1][4 * i + 3] = grid[i][j]

    return output

# the function that is called each time we want to print the board and each time we convert the grid and print it to the output
def print_board(grid):
    output = convert(grid)

    os.system('clear')
    for i in range(len(output)):
        for j in range(len(output[row])):
            if output[i][j]=="B":
                print(bcolors.OKBLUE+output[i][j]+ bcolors.ENDC,end="")
            elif output[i][j]=="E":
                print(bcolors.FAIL+output[i][j]+ bcolors.ENDC,end="")
            elif output[i][j]=="/" :
                print(bcolors.OKGREEN+output[i][j]+ bcolors.ENDC,end="")
            elif output[i][j]=="1" or output[i][j]=="2" or output[i][j]=="3" or output[i][j]=="e" or output[i][j]=="0":
                print(bcolors.WARNING+output[i][j]+bcolors.ENDC,end="")
            else:
                print(output[i][j],end="")
        print('\r')