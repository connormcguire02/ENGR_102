# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 5.4
# Date:         7 10 2022

#prompting the user to enter a 4 digit number
string_number = input("Enter a four-digit integer: ")
number = int(string_number)

# initializing the reversed numbers
string_backwards = ""
number_backwards = 0

string_backwards = string_number[len(string_number):0]