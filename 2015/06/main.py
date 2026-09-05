#!/usr/bin/env python3

"""
2015-06 Advent of Code
"""

"""
Notes:  
    https://www.reddit.com/r/adventofcode/comments/3vmltn/day_6_solutions/
"""


__author__ = "thewellington@gmail.com"
__version__ = ""
__license__ = ""

import numpy


def part_1(data):
    array = numpy.zeros((1000,1000), dtype=numpy.bool)
    for command in data.split("\n"):
        op, sx, sy = _parseCommand(command)
        if op == 'toggle':
            array[sx, sy] ^= 1
        else:
            array[sx, sy] = ['off', 'on'].index(op)
    return sum(sum(array))


def part_2(data):
    '''don't know if we need this yet'''



def main():
    """ Main entry point of the app """

    with open ('input.txt', 'r') as file:
        data = file
    print(data)
    for c in data.split("/n"):
        print(c)



   # part_1(data)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()


