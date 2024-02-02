#!/usr/bin/env python3

"""
2015/04 Advent of Code
"""

__author__ = "thewellington@gmail.com"
__version__ = ""
__license__ = ""

import hashlib
import re

secret_key = "yzbqklnj"

counter = 1

while counter > 0:
        
    mining_string = secret_key + str(counter)

    hash = hashlib.md5(mining_string.encode()).hexdigest()
    
    if re.search(r"(^00000\w+)", hash):
        print(str(counter) + ": " + hash)
        exit()
                
    counter += 1
    
    
def main():
    """ Main entry point of the app """
    
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
