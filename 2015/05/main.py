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

def vowel_count(string):
    get_vowels = [each for each in string if each in vowels]
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

def find_letter_pairs(string):
    result =  bool(re.search(r"(..).*\1", string))
    return result

def skip_repeat(string):
    result = bool(re.search(r"(.).\1", string))
    return result



def part_1(data):
    string_counter = 0

    for line in data:
       
        if find_double_chars(line) == True and vowel_count(line) == True:
            string_counter += 1
    
        if find_forbidden(line) == True:
            string_counter -= 1 

    print("Part 1 - " + str(string_counter) + " nice strings.")

def part_2(data):
    string_counter_2 = 0

    for line in data:
    
        if find_letter_pairs(line) == True and skip_repeat(line) == True:
            string_counter_2 += 1

    print("Part 2 - " + str(string_counter_2) + " nice strings.")

def main():
    """ Main entry point of the app """
    
    with open('input.txt', 'r') as file:
        data = file.readlines()

    part_1(data)

    part_2(data)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()


