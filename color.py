import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red')
print(text)
cprint('Hello, World!', 'green', 'on_red')