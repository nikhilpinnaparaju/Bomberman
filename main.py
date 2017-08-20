from grid import *
from inp import *
from bomb import *
from classdefs import *
from multiprocessing import Process

grid[1][1] = 'B'

bomber = bomberman()
timebomb = bomb()

bomber.bomb = timebomb

# print(bomber.bomb.time_left)
print_board(grid)
controller(bomber)