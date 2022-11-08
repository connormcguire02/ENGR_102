# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 2.8
# Date:         5 9 2022
from math import pi, floor
# here i am prompting the user to enter a number manually
print("Part 1:")
variable_time = 25
distance_initial = 2026
time_initial = 10
distance_final = 23026
time_final = 55
slope = (distance_final-distance_initial)/(time_final-time_initial)
variable_distance = slope*(variable_time-time_initial) + distance_initial
print("For t = "+ str(variable_time)+ " minutes, the position p = "+str(variable_distance)+ " kilometers")
print("Part 2:")
variable_time = 300
variable_distance = slope*(variable_time-time_initial) + distance_initial
radius_of_earth = 6745
circum_of_earth = 2*pi*radius_of_earth
# print(circum_of_earth)
multiple = variable_distance/circum_of_earth
multiple = floor(multiple)
variable_distance -= multiple*circum_of_earth
print("For t = "+ str(variable_time)+ " minutes, the position p = "+ str(variable_distance)+ " kilometers")