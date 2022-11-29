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
# importing necessary modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
from math import sin
from math import cos
from math import pi
# Setting up subplot to plot all 3 graphs.
plt.figure(figsize=(30, 10))
##### QUESTION 1 #####
plt.subplot(131)
# creating x and y values
x = np.linspace(-2.0, 2.0, 100)
y1 = (1/(4*2)) * (x ** 2)
y2 = (1/(4*6)) * (x ** 2)#y value 2

# labeling the plot
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Parabola with varying focal length")

# displaying the plot
q1_plot1 = plt.plot(x,y1, linewidth = 2, color = 'blue')
q1_plot2 = plt.plot(x,y2, linewidth = 6, color = 'red')

# creating a legend
red_patch = mpatches.Patch(color='red', label='f=6')
blue_patch = mpatches.Patch(color='blue', label='f=2')
plt.legend(handles=[red_patch, blue_patch])

##### Question 2 #####
plt.subplot(132)
# setting up x and y
x1 = np.linspace(-4.0, 4.0, 25)
q2_y = (2*x1**3) + (3*x1**2) - 11*x1 - 6
# labels 
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Plot of a cubic polynomial")
# displaying the plot
plt.scatter(x1,q2_y, linewidth = 1, marker ="*", color = "yellow", edgecolors = "black", s=500)

##### Question 3 #####
# sin #
plt.subplot(233)
x3 = np.linspace(-2*np.pi, 2 * np.pi, 200)
y = np.sin(x3)
plt.title("Graphs of sin(x) and cos(x)")
plt.grid()
plt.plot(x3, y, color='darkred')
red_patch = mpatches.Patch(color='darkred', label='y=sin(x)')
plt.legend(handles=[red_patch])
plt.ylabel("y = sin(x)")
plt.xticks(color='w')
# cos #


plt.subplot(236)
plt.ylabel("y = cos(x)")
plt.xlabel("X values")
plt.grid()
x3 = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.cos(x3)
blue_patch = mpatches.Patch(color='darkblue', label='y=cos(x)')
plt.legend(handles=[blue_patch])
plt.plot(x3, y, color='darkblue')
plt.show()
