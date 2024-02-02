#!/usr/bin/env python3

"""
2015/03 Advent of Code
"""

__author__ = "thewellington@gmail.com"
__version__ = ""
__license__ = ""


with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')

santas_directions = data[::2]
robo_santas_directions = data[1::2]

def route(directions):
    x, y = 0, 0
    houses_visited = set((x, y))
    houses_visited.remove(0)
    print(houses_visited)

    for d in directions:
        if d == ">":
            x += 1
        elif d == "<":
            x -= 1
        elif d == "^":
            y += 1
        elif d == "v":
            y -= 1
    
        current_coord = (x, y)
        houses_visited.add(current_coord)

    return(houses_visited)
    

def year_two():
    santa = route(santas_directions)
    robot = route(robo_santas_directions)
        
    houses_visited = santa.union(robot)
    houses_visited.discard(0) # this accounts for the extra zero coordinate fromt he union
    print(houses_visited)

    return(houses_visited)

    
    
def main():
    """ Main entry point of the app """
    print(len(route(data)))
    print(len(year_two()))
    
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
