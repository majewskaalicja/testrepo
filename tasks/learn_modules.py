'''
import function and run it
'''
from greeting import greeting

def print_name():
    print('Enter your name: ')
    name = input()
    greeting(name)

print_name()



