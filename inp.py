from getch import getch
import os
from grid import *
import datetime as timer
import time
import sys,select
import termios
import sys, tty

def controller(bomber):
    while 1:

        control = getch()
        
        # print(control)
        
        if (control):
        
            # print(sys.stdin.readline().strip())
            # sys.stdout.flush()
            if control=='q':
                break
            else:
                if control=='d':
                    if grid[bomber.location['x']][bomber.location['y']+1] != 'X':
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][bomber.location['y']] = ' '

                        grid[bomber.location['x']][bomber.location['y']+1] = 'B'
                        bomber.location['y'] = bomber.location['y']+1

                if control=='w':
                    if grid[bomber.location['x']-1][bomber.location['y']]!='X':
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][bomber.location['y']] = ' '
                        
                        grid[bomber.location['x']-1][bomber.location['y']] = 'B'
                        bomber.location['x'] = bomber.location['x']-1

                if control=='a':
                    if grid[bomber.location['x']][bomber.location['y']-1] != 'X':
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][bomber.location['y']] = ' '
                        
                        grid[bomber.location['x']][bomber.location['y']-1] = 'B'
                        bomber.location['y'] = bomber.location['y']-1

                if control=='s':
                    if grid[bomber.location['x']+1][bomber.location['y']] != 'X':
                        
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][bomber.location['y']] = ' '
                        
                        grid[bomber.location['x']+1][bomber.location['y']] = 'B'
                        bomber.location['x'] = bomber.location['x']+1

                if control=='b':
                    if bomber.bombs_left:
                        grid[bomber.location['x']][bomber.location['y']] = str(bomber.bomb.time_left)
                        bomber.bomb.location['x'] = bomber.location['x']
                        bomber.bomb.location['y'] = bomber.location['y']
                        bomber.bombs_left = bomber.bombs_left - 1
                        bomber.bomb.start()

        if (not(bomber.bomb.location['x']==None) and not(bomber.bomb.location['y']==None)):
            grid[bomber.bomb.location['x']][bomber.bomb.location['y']] = str(bomber.bomb.time_left)    

        if control == 'q':
            break

        os.system('clear')
        print_board(grid)

        print("you moved:",control)