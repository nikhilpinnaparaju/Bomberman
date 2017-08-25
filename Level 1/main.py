from grid import *
from inp import *
from classdefs import *
from multiprocessing import Process
from threader import *
import random
import os
import copy

# declaration of the bomberman on the grid
grid[1][1] = 'B'

# Creation of a bomberman object and a bomb object
bomber = bomberman()
timebomb = bomb()

bomber.bomb = timebomb

# print(bomber.bomb.time_left)

# declaration of a set of enemies
enemies = set()

# declaring some enemies
a = enemy()
b = enemy()
# c = enemy()

enemies.add(a)
enemies.add(b)
# enemies.append(c)

# adding the enemies to the grid
for i in enemies:
    # print(i.location['x'],i.location['y'])
    grid[i.location['x']][i.location['y']] = 'E'

# class declaration to start the async process of enemies movement


class movingEnemies(RepeatedTimer):

    def __init__(self):
        self.enemies = enemies
        RepeatedTimer.__init__(self, 1, moveEnemies, enemies)

# continously checks if there an overlap in position to see if any lives
# need to be lost be it enemy or bomberman


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
                    if (abs(enemy.location['x'] - bomber.bomb.location['x']) +
                            abs(enemy.location['y'] - bomber.bomb.location['y']) < 2):
                        # print("Enemy dies", end = '/r')
                        grid[enemy.location['x']][enemy.location['y']] = " "
                        if (enemy.life == 0):
                            enemies.discard(enemy)

                            if (len(enemies) == 0):
                                term = "All Enemies killed, Level Complete"
                                cprint(term, 'white', 'on_red')
                                os._exit(1)

                        else:
                            enemy.life = enemy.life - 1

                        # score = score + 100

        # if (bomber.bomb.location['x'] is not None):
        #     if (grid[bomber.bomb.location['x']+1][bomber.bomb.location['y']] == '/'):
        #         score = score + 20

        #     if (grid[bomber.bomb.location['x']-1][bomber.bomb.location['y']] == '/'):
        #         score = score + 20

        #     if (grid[bomber.bomb.location['x']][bomber.bomb.location['y']+1] == '/'):
        #         score = score + 20

        #     if (grid[bomber.bomb.location['x']][bomber.bomb.location['y']-1] == '/'):
        #         score = score + 20

        for enemy in repl:
            if ((bomber.location['x'] == enemy.location['x']) and
                    (bomber.location['y'] == enemy.location['y'])):
                if (bomber.life):
                    bomber.life = bomber.life - 1
                    grid[bomber.location['x']][bomber.location['y']] = " "
                    bomber.location['x'] = 1
                    bomber.location['y'] = 1
                    grid[1][1] = "B"

                elif (bomber.life == 0):
                    term = ("Game Over")
                    cprint(term, 'white', 'on_red')
                    os._exit(1)

        if (bomber.bomb.location['x'] is not None):
            if (bomber.bomb.time_left == -1):
                if (abs(bomber.location['x'] - bomber.bomb.location['x']) +
                        abs(bomber.location['y'] - bomber.bomb.location['y']) < 2):
                    if (bomber.life):
                        bomber.life = bomber.life - 1
                        grid[bomber.location['x']][bomber.location['y']] = " "
                        bomber.location['x'] = 1
                        bomber.location['y'] = 1
                        grid[1][1] = "B"

                    elif (bomber.life == 0):
                        term = ("Game Over")
                        cprint(term, 'white', 'on_red')
                        os._exit(1)

# starts the killing check function and the enemy movement function
scoring = killingFunction()
scoring.start()

randEnemyMove = movingEnemies()
randEnemyMove.start()

print_board(grid)
# final = colored("Lives: ",bomber.life, " Score: ",score,'white', 'on_red')
# cprint(final)

print("Lives: ", bomber.life, " Score: ", score)

controller(bomber)
