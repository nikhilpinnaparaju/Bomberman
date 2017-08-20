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
        self.location = {'x':None, 'y':None}
        RepeatedTimer.__init__(self,1,self.blast)

    def blast(self):
        if (self.time_left):
            self.time_left = self.time_left - 1

        else:
            self.stop()

class enemy(RepeatedTimer):
    def __init__(self):
        person.__init__(self)
        self.location = {'x':random.randrange(19), 'y':random.randrange(19)}
        
        while (grid[self.location['x']][self.location['y']]!=' '):
            self.location['x'] = random.randrange(19)
            self.location['y'] = random.randrange(19)

        # self.moveEnemies = moveEnemies

        RepeatedTimer.__init__(self,1,moveEnemies,self)