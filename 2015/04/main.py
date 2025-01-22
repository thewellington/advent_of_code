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


def miner( key, search_string ):

    counter = 1 
    regex = re.escape(search_string)   
    while counter > 0:
        mining_string = key + str(counter)
        hash = hashlib.md5(mining_string.encode()).hexdigest()
        if re.search(f"^{regex}\w+", hash): 
            result = (str(counter) + ": " + hash)
            return(result)

        counter += 1
    
    
def main():
    """ Main entry point of the app """
    
    print("the lowest hash beginning with five zeros is: ")
    result1 = miner(secret_key, "00000")
    print(result1)

    print("the lowest hash beginning with six zeros is: ")
    result2 = miner(secret_key, "000000")
    print(result2)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
