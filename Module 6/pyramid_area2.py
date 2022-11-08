# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 6.11
# Date:         10/07/22
#
# Gathering Inputs for Equation
from math import sqrt
# s = side_length
s = float(input('Enter the side length in meters: '))
# n = layers
n = int(input('Enter the number of layers: '))
# A1 = the first term in the sequence that the sum will be taken of
A1 = s ** 2 * ((sqrt(3) / 4) + 3)
# An = the last term in the sequence that the sum will be taken of
An = s ** 2 * ((sqrt(3) / 4) * (2 * n - 1) + 3 * n)
# Calculating the sum without using a loop using arithmetic progression
area = (A1 + An) / 2 * n
print(f'You need {area:.2f} m^2 of gold foil to cover the pyramid')