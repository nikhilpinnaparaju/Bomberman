from classdefs import *
import time

def blast():
    if (bomb.time_left>0):
        time.sleep(1)
        bomb.time_left = bomb.time_left - 1

    if not(bomb.time_left):
        bomb.Timer.stop()