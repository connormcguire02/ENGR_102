# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:        Connor McGuire
# Section:      563
# Assignment:   Lab 4.17: how_may_gadgets
# Date:         09/20/22
from math import sqrt

a = 1 / 7
print(f'a = {a}')
b = a * 7
print(f'b = a * 7 = {b}')

c = 2 * a
d = 5 * a
f = c + d
print(f'f = 2 * a + 5 * a = {f}')

x = sqrt(1 / 3)
print(f'x = {x}')
y = x * x * 3
print(f'y = x * x * 3 = {y}')
z = x * 3 * x
print(f'z = x * 3 * x = {z}')

TOL = 1e-10
# check if b and f are equal within specified tolerance
if abs(b - f) < TOL:
    print(f'b and f are equal within tolerance of {TOL}')
else:
    print(f'b and f are NOT equal within tolerance of {TOL}')