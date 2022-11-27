# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 11.11
# Date:         11 11 2022

# importing the necessary modules
import numpy as np
import matplotlib.pyplot as plt

# setting the inital set of x and y that will be plotted
x_set = [0]
y_set = [1]

# setting up the 2d arrays that will be multiplied together
v = np.matrix("0; 1")
M = np.matrix("1.01 0.09; -0.09 1.01")

# multiplyingthe matracies 200 times to manipulate the value of v
for _ in range(200):
    v = M @ v
    x_set += [v[0,0]]
    y_set += [v[1,0]]

# all of the pyplot is here
fig, ax = plt.subplots()
ax.scatter(x_set, y_set)
ax.set_xlabel("x-component")
ax.set_ylabel("y-component")
ax.set_title("Matrix Multiplication Spiral")

plt.show()
