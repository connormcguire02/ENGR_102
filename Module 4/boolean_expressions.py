# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 4.14: boolean_expressions
# Date:         09/23/22

############ Part A ############
a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

# converting T, t, and True, F, f, and False into True or False
if a == "True" or a == "T" or a == "t":
    a = True
else:
    a = False
if b == "True" or b == "T" or b == "t":
    b = True
else:
    b = False
if c == "True" or c == "T" or c == "t":
    c = True
else:
    c = False

############ Part B ############
# Outputting True/False based on the values entered
print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

############ Part C ############
# Outputting True if a or b is True but not if both are True or both are False
print(f"XOR: {(not a) and b or (not b) and a}")
# Outputting True if 1 or 3 of the variables are True, otherwise False
print(f"Odd number: {(a and b and c) or ((a or b or c) and not((a and b) or (b and c) or (c and a)))}")
