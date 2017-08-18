from getch import getch

while 1:
    control = getch()
    if control=='q':
        break
    else:
        print("you moved:",control)