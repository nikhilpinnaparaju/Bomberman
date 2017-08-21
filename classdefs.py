from threader import *
from grid import *
from inp import moveEnemies
import time
import random

class person():
    def __init__(self):
        self.life=1

class bomberman(person):
    def __init__(self):
        person.__init__(self)
        self.life=3
        self.location= {'x':1,'y':1}
        self.bombs_left = 1

class bomb(RepeatedTimer):
    def __init__(self):
        self.time_left = 3
        self.power = 1
        self.bombs_left = 1
        self.location = {'x':None, 'y':None}
        RepeatedTimer.__init__(self,1,self.blast)

    def blast(self):
        if (self.time_left>0):
            self.time_left = self.time_left - 1
            grid[self.location['x']][self.location['y']] = str(self.time_left)
        
        # if (not(self.location['x']==None) and not(self.location['y']==None)):
            # grid[self.location['x']][self.location['y']] = str(self.time_left)
        
        elif (self.time_left == 0):
            if grid[self.location['x']][self.location['y']] != 'X':
                grid[self.location['x']][self.location['y']] = 'e'
            
            if grid[self.location['x']+1][self.location['y']] !='X':
                grid[self.location['x']+1][self.location['y']] = 'e'
            
            if grid[self.location['x']][self.location['y']+1] != 'X':
                grid[self.location['x']][self.location['y']+1] = 'e'
            
            if grid[self.location['x']-1][self.location['y']] != 'X':
                grid[self.location['x']-1][self.location['y']] = 'e'
            
            if grid[self.location['x']][self.location['y']-1] != 'X':
                grid[self.location['x']][self.location['y']-1] = 'e'

            self.time_left = -1

        elif (self.time_left == -1):
            if grid[self.location['x']][self.location['y']] != 'X':
                grid[self.location['x']][self.location['y']] = ' '
            
            if grid[self.location['x']+1][self.location['y']] !='X':
                grid[self.location['x']+1][self.location['y']] = ' '
            
            if grid[self.location['x']][self.location['y']+1] != 'X':
                grid[self.location['x']][self.location['y']+1] = ' '
            
            if grid[self.location['x']-1][self.location['y']] != 'X':
                grid[self.location['x']-1][self.location['y']] = ' '
            
            if grid[self.location['x']][self.location['y']-1] != 'X':
                grid[self.location['x']][self.location['y']-1] = ' '

            self.time_left = 3
            self.location['x'] = None
            self.location['y'] = None
            self.bombs_left = self.bombs_left + 1
            self.stop()
        
        print_board(grid)

class enemy(RepeatedTimer):
    def __init__(self):
        person.__init__(self)
        self.location = {'x':random.randrange(19), 'y':random.randrange(19)}
        
        while (grid[self.location['x']][self.location['y']]!=' '):
            self.location['x'] = random.randrange(19)
            self.location['y'] = random.randrange(19)

        # self.moveEnemies = moveEnemies

        RepeatedTimer.__init__(self,1,moveEnemies,self)