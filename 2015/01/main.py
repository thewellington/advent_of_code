#!/usr/bin/env python3

"""
2015/01 Advent of Code
"""

__author__ = "thewellington@gmail.com"
__version__ = ""
__license__ = ""


with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')

def part1():
    up = data.count('(')
    down = data.count(')')
    floor = up - down
      
    return(int(floor))

def part2():
    floor = 0
    position = 0
    for c in data:
        position = position +1
        if c == '(':
            floor = floor + 1
        elif c == ')':
            floor = floor - 1
        
        if floor == -1:
            return(position)
        
    return(floor)

def main():
    """ Main entry point of the app """
    print("Santa is on floor " + str(part1()))

    print("Position " + str(part2()) + " puts Santa in the basement.")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
