# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 5.4
# Date:         6 10 2022

# importing math because we will need it
from math import sqrt

# prompting the user to enter a vector A
vector_a_input = input("Enter the elements for vector A: ")

# prompting the user to enter a vector B
vector_b_input = input("Enter the elements for vector B: ")

# seperating the components into a list using rsplit
vector_a = vector_a_input.rsplit(" ")
vector_b = vector_b_input.rsplit(" ")

# creating a while loop that traverses the list and casts all indecies to float
n = 0
while n < len(vector_a):
    vector_a[n] = float(vector_a[n])
    n += 1
n = 0
while n < len(vector_b):
    vector_b[n] = float(vector_b[n])
    n += 1
# computing the magnitude of each vector
n = 0
sum_squared_a = 0
sum_squared_b = 0

while n < len(vector_a):
    sum_squared_a += vector_a[n]**2
    n += 1
mag_a = sqrt(sum_squared_a)

n = 0
while n < len(vector_b):
    sum_squared_b += vector_b[n]**2
    n += 1
mag_b = sqrt(sum_squared_b)

# making sure that the vectors have the same length
n = len(vector_a) - len(vector_b)
if n > 0:
    for i in range(n):
        vector_b.append(0.0)
if n < 0:
    n = -1*n
    for i in range(n):
        vector_a.append(0.0)

# computing the resultant of the vectors
n = 0
resultant = []
while n < len(vector_a) and n < len(vector_b):
    resultant.append(vector_a[n] + vector_b[n])
    n += 1
# print(resultant)

# computing the difference of the vectors
n = 0
difference = []
while n < len(vector_a) and n < len(vector_b):
    difference.append(vector_a[n]-vector_b[n])
    n += 1
# print(difference)

# print(vector_a)
# print(vector_b)

# computing the dot product of the vectors
dot_product = 0
n = 0
while n < len(vector_a) and n < len(vector_b):
    dot_product += vector_a[n]*vector_b[n]
    n += 1
# print(dot_product)

print(f"The magnitude of vector A is {mag_a:.5f}")
print(f"The magnitude of vector B is {mag_b:.5f}")
print(f"A + B is {resultant}")
print(f"A - B is {difference}")
print(f"The dot product is {dot_product:.2f}")