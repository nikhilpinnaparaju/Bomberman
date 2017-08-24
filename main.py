from grid import *
from inp import *
from classdefs import *
from multiprocessing import Process
from threader import *
import random

grid[1][1] = 'B'

bomber = bomberman()
timebomb = bomb()

bomber.bomb = timebomb

# RepeatedTimer.__init__()

# print(bomber.bomb.time_left)

enemies = set()

a = enemy()
# b = enemy()
# c = enemy()

enemies.add(a)
# enemies.append(b)
# enemies.append(c)

for i in enemies:
    # print(i.location['x'],i.location['y'])
    grid[i.location['x']][i.location['y']] = 'E'
    i.start()

print_board(grid)
controller(bomber)