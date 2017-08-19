from getch import getch
import os
from grid import *

def controller(bomber):
    while 1:
        control = getch()

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
                grid[bomber.location['x']][bomber.location['y']] = 'b'

            os.system('clear')
            print_board(grid)

            print("you moved:",control)