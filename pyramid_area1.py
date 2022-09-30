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

# Gathering Inputs for Equation
from math import sqrt
# s = side_length
s = float(input('Enter the side length in meters: '))
# n = layers
n = int(input('Enter the number of layers: ')) 
# set area as a variable
area = 0

for i in range(n):
  # equation to calculate surface area needed to cover the pyramid, created based on the given pyramid imagee
  area += (sqrt(3) / 4) * s ** 2 * (2 * (i + 1) - 1) + 3 * (i + 1) * s ** 2 

print(f'You need {area:.2f} m^2 of gold foil to cover the pyramid')