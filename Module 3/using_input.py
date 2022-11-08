# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 3.17
# Date:         12 9 2022
from math import sin, pi
print("This program calculates the applied force given mass and acceleration ")
# prompting the user to enter a mass that will be initially stored as a string
mass = input("Please enter the mass (kg): ")
# casting mass to a float
mass = float(mass)
# prompting the user to enter an acceleration that will be initally stored as a string
acceleration = input("Please enter the acceleration (m/s^2): ")
# casting acceleration to a float
acceleration = float(acceleration)
# calculating applied force on an object of prompted mass and acceleration
force = mass * acceleration
print(f"Force is {force: .1f} N")

print("This program calculates the wavelength given distance and angle")
# B) Bragg's Law
# n is the diffraction order
diffraction_order = 1
# Prompting the user to input a distance
distance = input("Please enter the distance (nm): ")
# Casting distance to a float
distance = float(distance)

# prompting the user to input an angle
theta = input("Please enter the angle (degrees): ")
theta = float(theta)
# theta is in degrees but math.sin() takes arguments in radians
theta = theta*pi/180
# now theta is in radians

# solving for wavelength

wavelength = 2*distance*sin(theta)/diffraction_order
print(f"Wavelength is {wavelength: .4f} nm")

print("This program calculates how much Radon-222 is left given time and initial amount")
# C) Radioactive decay

# t is the time of decay in days
# Prompting the user to input a time interval
time = input("Please enter the time (days): ")
time = float(time)

# N0 is initial mass in g
# Prompting the user to enter an initial mass in g
initial_mass = input("Please enter the initial amount (g): ")
# Casting initial mass to a float
initial_mass = float(initial_mass)

# half-life of Radon-222 in days
half_life = 3.8 # days

# N is the amount of mass after t time of decay
final_mass = 2 ** ((-1)*time/half_life) # g
final_mass *= initial_mass
print(f"Radon-222 left is {final_mass: .2f} g")

print("This program calculates the pressure given moles, volume, and temperature")
# D) Ideal Gas Law
# PV=nRT
# amount of substance measured in moles
# Prompting the user to enter the amount of substance of the gas
amount_of_substance = input("Please enter the number of moles: ")
# Casting amount_of_substance to a float
amount_of_substance = float(amount_of_substance)

# volume measured in m^3
# Prompting the user to enter a volume
volume = input("Please enter the volume (m^3): ")
# Casting volume to a float
volume = float(volume)

# R is the ideal gas constant measured in m^3Pa/K*mol
ideal_gas_constant = 8.314

# T is temperature measured in Kelvin
# Prompting the user to enter a temperature
temperature = input("Please enter the temperature (K): ")
# Casting temperature to a float
temperature = float(temperature)

# The given ideal gas law constant uses pressure unit Pa so we will need to convert our pressure into kPa
pressure = amount_of_substance*ideal_gas_constant*temperature/(volume*1000)
print(f"Pressure is {pressure: .0f} kPa")