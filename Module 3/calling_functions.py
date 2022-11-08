# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 3.18
# Date:         13 9 2022

from math import *


def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')


# Prompting the user to enter a side length that will be used find area
# These shapes will all be regular polygons
side_length = input("Please enter the side length: ")
# Casting side_length to a float
side_length = float(side_length)

# Calculating the area of a regular triangle using the input side length
area = sqrt(3)/4 * (side_length**2)
printresult("triangle", side_length, area)

# Calculating the area of a regular square
area = side_length **2
printresult("square", side_length, area)

# Calculating the area of a regular pentagon using the input side length
area = (1/4)* sqrt(5*(5+(2*sqrt(5))))* (side_length**2)
printresult("pentagon", side_length, area)

# Calculating the area of a regular dodecagon using the input side length
area = 3 * (2 + sqrt(3)) * (side_length**2)
printresult("dodecagon", side_length, area)
