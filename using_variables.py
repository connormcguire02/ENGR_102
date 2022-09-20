# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 1.11
# Date:         5 9 2022
from math import sin, pi

# A) Newton's Second Law of Motion to calculate force
mass = 3

acc = 5.5 # acc in m/s^2
# F=ma
force = mass*acc # N
print("Force is "+ str(force)+ " N")

# B) Bragg's Law
# n is the diffraction order
diffraction_order = 1

distance = 0.025 # distance in nm

# theta is in degrees but math.sin() takes arguments in radians
theta = 25*pi/180
# now theta is in radians

# solving for wavelength

wavelength = 2*distance*sin(theta)/diffraction_order
print("Wavelength is "+ str(wavelength)+ " nm")

# C) Radioactive decay
# N0 is initial mass in g
initial_mass = 5

# t is the time of decay in days
time = 3 # days

# half is the half-life of Radon-222 in days
half_life = 3.8 # days

# N is the amount of mass after t time of decay
final_mass = 2 ** ((-1)*time/half_life) # g
final_mass *= initial_mass
print("Radon-222 left is "+ str(final_mass)+ " g")

# D) Ideal Gas Law
# PV=nRT

# volume measured in m^3
volume = 0.25

# amount of substance measured in moles
amount_of_substance = 5

# R is the ideal gas constant measured in m^3Pa/K*mol
ideal_gas_constant = 8.314

# T is temperature measured in Kelvin
temperature = 415

# The given ideal gas law constant uses pressure unit Pa so we will need to convert our pressure into kPa
pressure = amount_of_substance*ideal_gas_constant*temperature/(volume*1000)
print("Pressure is "+ str(pressure) +" kPa")