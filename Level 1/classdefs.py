from threader import *
from grid import *
from inp import moveEnemies
import time
import random

# Person Class is the fundamental class that all characters are built upon
# being enemies and Bomberman


class person():

    def __init__(self):
        self.life = 1

# The Class declaring the main, playable character of the game being bomberman
# Has the attributes of the no. of bombs the player has left, and the location
# is a dictionary along with the number of lifes
# This is direct use of the concept of inheritance


class bomberman(person):

    def __init__(self):
        person.__init__(self)
        self.life = 3
        self.location = {'x': 1, 'y': 1}
        self.bombs_left = 1

# The RepeatedTimer class has been declared in the threader.py file
# the class declaring the main weapon of bomberman which is the bomb. It takes
# in a class RepeatedTimer which is used for threading
# has a power attribute which tells us blast radius and the time_left to
# detonation. The remaining  attributes are similar to the bomberman class
# the bomb class has a function blast inside it that explains how the bomb
# blast works in the game Bomb works asynchronous to the bomberman


class bomb(RepeatedTimer):

    def __init__(self):
        self.time_left = 3
        self.power = 1
        self.bombs_left = 1
        self.location = {'x': None, 'y': None}
        RepeatedTimer.__init__(self, 1, self.blast)

    def blast(self):
        if (self.time_left > 0):
            self.time_left = self.time_left - 1
            grid[self.location['x']][self.location['y']] = str(self.time_left)

        elif (self.time_left == 0):
            if grid[self.location['x']][self.location['y']] != 'X':
                grid[self.location['x']][self.location['y']] = 'e'

            if grid[self.location['x'] + 1][self.location['y']] != 'X':
                grid[self.location['x'] + 1][self.location['y']] = 'e'

            if grid[self.location['x']][self.location['y'] + 1] != 'X':
                grid[self.location['x']][self.location['y'] + 1] = 'e'

            if grid[self.location['x'] - 1][self.location['y']] != 'X':
                grid[self.location['x'] - 1][self.location['y']] = 'e'

            if grid[self.location['x']][self.location['y'] - 1] != 'X':
                grid[self.location['x']][self.location['y'] - 1] = 'e'

            self.time_left = -1

        elif (self.time_left == -1):
            if grid[self.location['x']][self.location['y']] != 'X':
                grid[self.location['x']][self.location['y']] = ' '

            if grid[self.location['x'] + 1][self.location['y']] != 'X':
                grid[self.location['x'] + 1][self.location['y']] = ' '

            if grid[self.location['x']][self.location['y'] + 1] != 'X':
                grid[self.location['x']][self.location['y'] + 1] = ' '

            if grid[self.location['x'] - 1][self.location['y']] != 'X':
                grid[self.location['x'] - 1][self.location['y']] = ' '

            if grid[self.location['x']][self.location['y'] - 1] != 'X':
                grid[self.location['x']][self.location['y'] - 1] = ' '

            self.stop()
            self.time_left = 3
            self.location['x'] = None
            self.location['y'] = None
            self.bombs_left = self.bombs_left + 1

        print_board(grid)

# The enemy class also takes the RepeatedTimer class which works allows
# it to work asynchronous to the bomberman and his bombs
# The enemy are spawned randomly and take an empty place on the board


class enemy(RepeatedTimer):

    def __init__(self):
        person.__init__(self)
        self.location = {'x': random.randrange(19), 'y': random.randrange(19)}

        while (grid[self.location['x']][self.location['y']] != ' '):
            self.location['x'] = random.randrange(19)
            self.location['y'] = random.randrange(19)
