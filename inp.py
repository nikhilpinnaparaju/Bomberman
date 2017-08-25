from getch import getch
import os
from grid import *
import datetime as timer
import time
import sys
import select
import termios
import sys
import tty
import random


def controller(bomber):
    while bomber.life:

        control = getch()

        print(control)

        if (control):
            if control == 'q':
                break

            else:
                if control == 's':
                    if (grid[bomber.location['x']][bomber.location['y'] + 1] !=
                        'X' and
                            grid[bomber.location['x']][bomber.location['y'] + 1] != '/'):
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][
                                bomber.location['y']] = ' '

                        grid[bomber.location['x']][
                            bomber.location['y'] + 1] = 'B'
                        bomber.location['y'] = bomber.location['y'] + 1

                if control == 'a':
                    if (grid[bomber.location['x'] - 1][bomber.location['y']] !=
                        'X' and
                            grid[bomber.location['x'] - 1][bomber.location['y']] != '/'):
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][
                                bomber.location['y']] = ' '

                        grid[bomber.location['x'] -
                             1][bomber.location['y']] = 'B'
                        bomber.location['x'] = bomber.location['x'] - 1

                if control == 'w':
                    if (grid[bomber.location['x']][bomber.location['y'] - 1] !=
                        'X' and
                            grid[bomber.location['x']][bomber.location['y'] - 1] != '/'):
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][
                                bomber.location['y']] = ' '

                        grid[bomber.location['x']][
                            bomber.location['y'] - 1] = 'B'
                        bomber.location['y'] = bomber.location['y'] - 1

                if control == 'd':
                    if (grid[bomber.location['x'] + 1][bomber.location['y']] !=
                        'X' and
                            grid[bomber.location['x'] + 1][bomber.location['y']] != '/'):

                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][
                                bomber.location['y']] = ' '

                        grid[bomber.location['x'] +
                             1][bomber.location['y']] = 'B'
                        bomber.location['x'] = bomber.location['x'] + 1

                if control == 'b':
                    if bomber.bomb.bombs_left:
                        grid[bomber.location['x']][bomber.location[
                            'y']] = str(bomber.bomb.time_left)
                        bomber.bomb.location['x'] = bomber.location['x']
                        bomber.bomb.location['y'] = bomber.location['y']
                        bomber.bomb.bombs_left = bomber.bomb.bombs_left - 1
                        bomber.bomb.start()

        # if (not(bomber.bomb.location['x']==None) and not(bomber.bomb.location['y']==None)):
            # grid[bomber.bomb.location['x']][bomber.bomb.location['y']] = str(bomber.bomb.time_left)

        if control == 'q':
            break

        print_board(grid)

    os._exit(1)
    # print("you moved:",control)


def moveEnemies(enemy):
    q = random.randrange(3)

    if (q == 0):
        if (grid[enemy.location['x']][enemy.location['y'] + 1] != 'X' and grid[enemy.location['x']][enemy.location['y'] + 1] != '/'):
            if grid[enemy.location['x']][enemy.location['y']] == 'E':
                grid[enemy.location['x']][enemy.location['y']] = ' '

            grid[enemy.location['x']][enemy.location['y'] + 1] = 'E'
            enemy.location['y'] = enemy.location['y'] + 1

    if (q == 1):
        if (grid[enemy.location['x'] - 1][enemy.location['y']] != 'X' and grid[enemy.location['x'] - 1][enemy.location['y']] != '/'):
            if grid[enemy.location['x']][enemy.location['y']] == 'E':
                grid[enemy.location['x']][enemy.location['y']] = ' '

            grid[enemy.location['x'] - 1][enemy.location['y']] = 'E'
            enemy.location['x'] = enemy.location['x'] - 1

    if (q == 2):
        if (grid[enemy.location['x'] + 1][enemy.location['y']] != 'X' and grid[enemy.location['x'] + 1][enemy.location['y']] != '/'):
            if grid[enemy.location['x']][enemy.location['y']] == 'E':
                grid[enemy.location['x']][enemy.location['y']] = ' '

            grid[enemy.location['x'] + 1][enemy.location['y']] = 'E'
            enemy.location['x'] = enemy.location['x'] + 1

    if (q == 3):
        if (grid[enemy.location['x']][enemy.location['y'] - 1] != 'X' and grid[enemy.location['x']][enemy.location['y'] - 1] != '/'):
            if grid[enemy.location['x']][enemy.location['y']] == 'E':
                grid[enemy.location['x']][enemy.location['y']] = ' '

            grid[enemy.location['x']][enemy.location['y'] - 1] = 'E'
            enemy.location['y'] = enemy.location['y'] - 1

    print_board(grid)
