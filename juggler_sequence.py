# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 5.4
# Date:         29 9 2022
from math import floor

# prompt the user to enter a number
n = int(input("Enter a positive integer: "))
print(f"The Juggler sequence starting at {n} is:")

n_string = str(n)

while n != 1:
    if n % 2 == 0:
        n
