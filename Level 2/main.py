from grid import *
from inp import *
from classdefs import *
from multiprocessing import Process
from threader import *
import random
import os
import copy

grid[1][1] = 'B'

bomber = bomberman()
timebomb = bomb()

bomber.bomb = timebomb

# print(bomber.bomb.time_left)

enemies = set()

a = enemy()
b = enemy()
# c = enemy()

enemies.add(a)
enemies.add(b)
# enemies.append(c)

for i in enemies:
    # print(i.location['x'],i.location['y'])
    grid[i.location['x']][i.location['y']] = 'E'

class movingEnemies(RepeatedTimer):
    def __init__(self):
        self.enemies = enemies
        RepeatedTimer.__init__(self, 0.5, moveEnemies, enemies)

class killingFunction(RepeatedTimer):

    def __init__(self):
        self.enemies = enemies
        self.bomber = bomber
        RepeatedTimer.__init__(self, 0.6, self.kill)

    def kill(self):
        repl = set()

        for i in enemies:
            repl.add(i)

        bomber = self.bomber

        if (bomber.bomb.location['x'] is not None):
            for enemy in repl:
                if (bomber.bomb.time_left == -1):
                    if (abs(enemy.location['x'] - bomber.bomb.location['x']) + abs(enemy.location['y'] - bomber.bomb.location['y']) < 2):
                        # print("Enemy dies", end = '/r')
                        grid[enemy.location['x']][enemy.location['y']] = " "
                        if (enemy.life == 0):
                            enemies.discard(enemy)

                        else:
                            enemy.life = enemy.life - 1

        for enemy in repl:
            if ((bomber.location['x'] == enemy.location['x']) and (bomber.location['y'] == enemy.location['y'])):
                if (bomber.life):
                    bomber.life = bomber.life - 1
                    grid[bomber.location['x']][bomber.location['y']] = " "
                    bomber.location['x'] = 1
                    bomber.location['y'] = 1
                    grid[1][1] = "B"

                elif (bomber.life == 0):
                    print("Game Over")
                    os._exit(1)

        if (bomber.bomb.location['x'] is not None):
            if (bomber.bomb.time_left == -1):
                # print("Bomber.x: ",bomber.location['x'], " Bomb.x: ",bomber.bomb.location['x']," Bomber.y: ",bomber.location['y']," Bomb.y: ",bomber.bomb.location['y'])
                if (abs(bomber.location['x'] - bomber.bomb.location['x']) + abs(bomber.location['y'] - bomber.bomb.location['y']) < 2):
                    # print((bomber.location['x'] - bomber.bomb.location['x']) + (bomber.location['y'] - bomber.bomb.location['y']))
                    if (bomber.life):
                        # print("Bomber loses life",end = '/r')
                        bomber.life = bomber.life - 1
                        grid[bomber.location['x']][bomber.location['y']] = " "
                        bomber.location['x'] = 1
                        bomber.location['y'] = 1
                        grid[1][1] = "B"

                    elif (bomber.life == 0):
                        print("Game Over")
                        os._exit(1)

scoring = killingFunction()
scoring.start()

randEnemyMove = movingEnemies()
randEnemyMove.start()

print_board(grid)
controller(bomber)
