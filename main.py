from grid import *
from inp import *
from classdefs import *
from multiprocessing import Process
import random

grid[1][1] = 'B'

bomber = bomberman()
timebomb = bomb()

bomber.bomb = timebomb

# print(bomber.bomb.time_left)

enemies = []

a = enemy()
# b = enemy()
# c = enemy()

enemies.append(a)
# enemies.append(b)
# enemies.append(c)

for i in enemies:
    # print(i.location['x'],i.location['y'])
    grid[i.location['x']][i.location['y']] = 'E'
    i.start()

print_board(grid)
controller(bomber)