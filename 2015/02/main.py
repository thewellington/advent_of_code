#!/usr/bin/env python3

"""
2015/02 Advent of Code
"""

__author__ = "thewellington@gmail.com"
__version__ = ""
__license__ = ""


with open('input.txt', 'r') as file:
    data = file.readlines()


def solution():
    total_paper_area = 0
    total_ribbon_length = 0
    for line in data:
        raw_dimensions = line.split('x')
        length = int(raw_dimensions[0])
        width = int(raw_dimensions[1])
        height = int(raw_dimensions[2])
        
        # get area of each face
        face_x = length * width
        face_y = length * height
        face_z = width * height
        
        # multiply faces by 2 (because this is a rectangular prisim)
        face_xx = face_x * 2
        face_yy = face_y * 2
        face_zz = face_z * 2
        
        # calculate the extra (area of smallest face)
        faces = [face_x, face_y, face_z]
        extra = min(faces)
        
        package_area = face_xx + face_yy + face_zz + extra
        
        total_paper_area = total_paper_area + package_area
        
        # and now for part 2
        dimensions = [length, width, height]
        dimensions.sort() # from smallest to largest
        smallest = dimensions[0]
        small = dimensions[1]
        wrap = smallest * 2 + small * 2
        bow = length * width * height
        ribbon = wrap + bow
        
        total_ribbon_length = total_ribbon_length + ribbon
        
        
    return(total_paper_area, total_ribbon_length)




def main():
    """ Main entry point of the app """
    paper, ribbon = solution()
    
    
    print("The elves requre " + str(paper) + " square feet of wrapping paper and " + str(ribbon) + " feet of ribbon")

#     print("Position " + str(part2()) + " puts Santa in the basement.")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
