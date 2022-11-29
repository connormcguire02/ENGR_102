# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 12.14
# Date:         11/15/22

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

from numpy import *
A = array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
B = array([[0, 1], [2, 3], [4, 5], [6, 7]])
C = array([[0, 1, 2], [3, 4, 5]])
print(f'A = {A}')
print()
print(f'B = {B}')
print()
print(f'C = {C}')
print()
D = A @ B @ C
print(f'D = {D}')
print()
print(f'D^T = {transpose(D)}')
print()
E = sqrt(D) / 2
print(f'E = {E}')