from grid import *
from inp import *

grid[1][1] = 'B'

class person():
    def __init__(self):
        self.life=1
        self.location= {'x':1,'y':1}

class bomberman(person):
    def __init__(self):
        person.__init__(self)
        self.life=3

bomber = bomberman()

print_board(grid)

controller(bomber)