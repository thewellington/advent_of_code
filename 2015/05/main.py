#!/usr/bin/env python3

"""
2015/05 Advent of Code
"""

__author__ = "thewellington@gmail.com"
__version__ = ""
__license__ = ""



vowels = "AaEeIiOoUu"
forbidden_pairs = ["ab", "cd", "pq", "xy"]

'''
def string_parser():
    for line in input.txt
        regex search for each forbidden_pairs
        remove line from output
        
    for line in output
        get vowels in each string
            for lines with more than three vowels, add to new output
            
    for line in new output
        get lines that contain at least one repeated letter
        https://stackoverflow.com/questions/64629528/counting-repeated-characters-in-a-string-in-a-row-python    
''' 
    
    
   

   
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