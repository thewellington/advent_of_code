#!/usr/bin/env python3

"""
2015/05 Advent of Code
"""

__author__ = "thewellington@gmail.com"
__version__ = ""
__license__ = ""



vowels = "AaEeIiOoUu"
forbidden = ["ab", "cd", "pq", "xy"]
    
def main():
    """ Main entry point of the app """

with open('input.txt', 'r') as file:
    data = file.readlines()
    
for string in data:
    get_vowels = [each for each in string if each in vowels]
    if len(get_vowels) >= 3:
        print(len(get_vowels))
    
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()


""" still need to take care of second and third cases """