from grid import *
from inp import *
from classdefs import *

grid[1][1] = 'B'

bomber = bomberman()
timebomb = bomb()

bomber.bomb = timebomb

# print(bomber.bomb.time_left)
print_board(grid)

controller(bomber)