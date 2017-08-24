from grid import *
from inp import *
from classdefs import *
from multiprocessing import Process
from threader import *
import random
import os

grid[1][1] = 'B'

bomber = bomberman()
timebomb = bomb()

bomber.bomb = timebomb

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

class killingFunction(RepeatedTimer):

    def kill(self,enemies,bomber):
        print("KILLLLLLLLL")

        repl = enemies
        for enemy in repl:
            if ((grid[enemy.location['x']] - grid[bomber.bomb.location['x']]) - (grid[enemy.location['y']] - grid[bomber.bomb.location['y']]) < 2):
                grid[enemy.location['x']][enemy.location['y']] = " "
                enemy.stop()
                enemies.discard(enemy)

        if ((grid[bomber.location['x']] - grid[bomber.bomb.location['x']]) - (grid[bomberman.location['y']] - grid[bomber.bomb.location['y']]) < 2) and bomber.life: 
            bomber.life = bomber.life - 1
            grid[bomber.location['x']][bomber.location['y']] = " "
            bomber.location['x'] = 1
            bomber.location['y'] = 1
            grid[1][1] = "B"

        elif (bomber.life == 0):
            printf("Game Over")
            os._exit(1)

    def __init__(self):
        RepeatedTimer.__init__(self,1,self.kill,enemies,bomber)
        self.enemies = enemies
        self.bomber = bomber

scoring = killingFunction()

print_board(grid)
controller(bomber)