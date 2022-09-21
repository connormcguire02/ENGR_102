# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:        Connor McGuire
# Section:      563
# Assignment:   Lab 4.16: how_may_gadgets
# Date:         09/20/22

# prompt the user to enter 3 different numbers
number_one =   float(input("Enter number 1: "))
number_two =   float(input("Enter number 2: "))
number_three = float(input("Enter number 3: "))

# using if statements to determine the largest number
if number_one > number_two and number_one > number_three:
    print(f"The largest number is {number_one}")
if number_two > number_one and number_two > number_three:
    print(f"The largest number is {number_two}")
if number_three > number_one and number_three > number_two:
    print(f"The largest number is {number_three}")

