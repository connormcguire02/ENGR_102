# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 1.11
# Date:         30 8 2022
from math import pow
print("This shows the evaluation of (x^2-1)/(x-1) evaluated close to x=1")
print("My guess is 2")
i = 8
x = 0
n = 1
# This while loop will go through 8 calculations of f(x) using a number that gets closer and closer to 1
while i > 0:
    x = 1 + pow(10, -n)
    y = ((x ** 2)-1)/(x-1)
    print(y)
    i -= 1
    n += 1

print()
print("My guess was spot on.")
