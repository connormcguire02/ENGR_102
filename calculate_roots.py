# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:        Connor McGuire
# Section:      563
# Assignment:   Lab 4.19: calculate_roots
# Date:         09/20/22
from math import sqrt
# prompting the user to input 3 different coefficients

a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))
x1 = 0
x2 = 0

# creating a series of if statements to determine what kind of relationship the function is

# if all coeifficients are zero then 0 always = 0
if a == b == c == 0:
    print("All real numbers")
    exit()

# if a and b are zero and c is not then c cannot equal zero ever
if a == b == 0 and c > 0:
    print("You entered an invalid combination of coefficients!")
    exit()

# Now I am going to single out all the linear equations when a = 0
if a == 0:
    x1 = -1*c/b
    print(f"The root is x = {x1:.1f}")
    exit()

# ok so now we have the easy ones out of the way
# I am going to be using the quadratic formula because the discriminant easily shows us what the roots look like
discriminant = b**2 - 4*a*c
# for two real number output
if discriminant > 0:
    x1 = (-1*b + sqrt(discriminant))/(2*a)
    x2 = (-1 * b - sqrt(discriminant)) / (2 * a)
    if x1 > x2:
        print(f"The roots are x = {x1:.1f} and x = {x2:.1f}")
    else:
        print(f"The roots are x = {x2:.1f} and x = {x1:.1f}")
# for two complex number output
if discriminant < 0:
    discriminant *= -1
    discriminant = sqrt(discriminant)
    print(f"The roots are x = {-1*b/(2*a)} + {discriminant/(2*a):.1f}i and x = {-1*b/(2*a)} - {discriminant/(2*a):.1f}i")

# now lets test for discriminant equalling zero
if discriminant == 0:
    print(f"The root is x = {-1*b/(2*a):.1f}")