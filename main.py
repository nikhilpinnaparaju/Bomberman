from grid import *
from input import *

grid[1][1] = 'B'

class person():
    def __init__(self):
        self.life=1
        self.location= {'x':1,'y':1}

bomber = person()

print_board(grid)