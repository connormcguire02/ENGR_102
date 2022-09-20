# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 1.11
# Date:         30 8 2022
from math import sin, pi

# A) Newton's Second Law of Motion
# mass in kg
mass = 3

# acc in m/s^2
acc = 5.5
# F=ma
force = mass*acc
print("Force is "+ str(force)+ " N")

# B) Bragg's Law
# n is the diffraction order
n = 1

# d is distance in nm
d = 0.025

# theta is in degrees but math.sin() takes arguments in radians
theta = 25*pi/180
# now theta is in radians
# solving for wavelength
wavelength = 2*d*sin(theta)/n
print("Wavelength is "+ str(wavelength)+ " nm")

# C) Radioactive decay
# N0 is initial mass in g
N0 = 5

# t is the time of decay in days
t = 3

# half is the half-life of Radon-222 in days
half = 3.8

# N is the amount of mass after t time of decay
N = 2 ** ((-1)*t/half)
N *= N0
print("Radon-222 left is "+ str(N)+ " g")

# D) Ideal Gas Law
# PV=nRT

# V is volume measured in m^3
V = 0.25

# n is amount of substance measured in moles
n = 5

# R is the ideal gas constant measured in m^3Pa/K*mol
R = 8.314

# T is temperature measured in Kelvin
T = 415

# The given ideal gas law constant uses pressure unit Pa so we will need to convert our pressure into kPa
P = n*R*T/(V*1000)
print("Pressure is "+ str(P) +" kPa")