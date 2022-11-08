# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 3.19
# Date:         13 9 2022

# This is just a test to see if github automatically updates my files

from math import e
# Prompting the user to input the number of decimal places they want for euler's number
precision = input("Please enter the number of digits of precision for e: ")
precision = int(precision)
print(f"The value of e to {precision} digits is: {e:.{precision}f}")
