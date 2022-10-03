# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 5.4
# Date:         29 9 2022
from math import floor, sqrt

# prompt the user to enter a number
n = int(input("Enter a positive integer: "))
print(f"The Juggler sequence starting at {n} is:")

n_string = str(n)

# using a loop to find all the terms in the sequence
i = 0
while n != 1:
    if n % 2 == 0:
        n = floor(sqrt(n))
        n_string += ", "+str(n)
    else:
        n = floor(n ** (3/2))
        n_string += ", "+str(n)
    i += 1

print(n_string)
print(f"It took {i} iterations to reach 1")