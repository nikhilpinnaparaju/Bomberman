from getch import getch
import os
from grid import *
import datetime as timer
import time
import sys,select

def controller(bomber):
    while 1:
        total_time = 0
        start = timer.datetime.now()
        stop = start

        while ((stop - start).microseconds < 10000):
            control = getch()

            sys.stdout.flush()

            if control=='q':
                break
            else:
                if control=='d':
                    if grid[bomber.location['x']][bomber.location['y']+1] == ' ':
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][bomber.location['y']] = ' '

                        grid[bomber.location['x']][bomber.location['y']+1] = 'B'
                        bomber.location['y'] = bomber.location['y']+1

                if control=='w':
                    if grid[bomber.location['x']-1][bomber.location['y']]==' ':
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][bomber.location['y']] = ' '
                        
                        grid[bomber.location['x']-1][bomber.location['y']] = 'B'
                        bomber.location['x'] = bomber.location['x']-1

                if control=='a':
                    if grid[bomber.location['x']][bomber.location['y']-1] == ' ':
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][bomber.location['y']] = ' '
                        
                        grid[bomber.location['x']][bomber.location['y']-1] = 'B'
                        bomber.location['y'] = bomber.location['y']-1

                if control=='s':
                    if grid[bomber.location['x']+1][bomber.location['y']] == ' ':
                        
                        if grid[bomber.location['x']][bomber.location['y']] == 'B':
                            grid[bomber.location['x']][bomber.location['y']] = ' '
                        
                        grid[bomber.location['x']+1][bomber.location['y']] = 'B'
                        bomber.location['x'] = bomber.location['x']+1

                if control=='b':
                    if bomber.bombs_left:
                        grid[bomber.location['x']][bomber.location['y']] = str(bomber.bomb.time_left)
                        bomber.bombs_left = bomber.bombs_left - 1

            stop = timer.datetime.now()

        if control == 'q':
            break
        
        total_time = total_time + 0.1
        print("total time is ",total_time)

        if (total_time-1 == 0):
            bomber.bomb.time_left = bomber.bomb.time_left - 1

        os.system('clear')
        print_board(grid)

        print("you moved:",control)