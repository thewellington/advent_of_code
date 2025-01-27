#!/usr/bin/env python3

"""
2015/05 Advent of Code
"""

__author__ = "thewellington@gmail.com"
__version__ = ""
__license__ = ""

import re

vowels = "AaEeIiOoUu"
forbidden_strings = ["ab", "cd", "pq", "xy"]


def old_vowel_count(): 
    for string in data:
        get_vowels = [each for each in string if each in vowels]
        if len(get_vowels) >= 3:
            print(len(get_vowels))
            return true

def vowel_count(string):
    get_vowels = [each for each in string if each in vowels]
        get vowels in each string
    result = bool(len(get_vowels) >= 3)
    return result

def find_double_chars(string):
    result = bool(re.search(r"(.)\1", string))
    return result

def find_forbidden(string):
    for f in forbidden_strings:
        forbidden = string.find(f)
        if forbidden == -1:
            return False
        else:
            return True

def main():
    """ Main entry point of the app """

    string_counter = 0

    with open('input.txt', 'r') as file:
        data = file.readlines()

    for line in data:
        print(line)
        if find_forbidden(line) == True:
            print("forbidden")
        
        if find_double_chars(line) == True and vowel_count(line) == True:
            string_counter += 1
       
    print(string_counter)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()


