# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 5.4
# Date:         28 9 2022

from math import log
# Prompting the user to enter an excess temperature
variable_excess_heat = float(input("Enter the excess temperature: "))

# Now I will have a list of if statements that corresponds to each stage of boiling

# if user inputs an invalid number
if variable_excess_heat < 1.3:
    print("Surface heat flux is not available ")

# Free convection stage
if 1.3 < variable_excess_heat < 5:
    initial_heat_flux = 1000.0
    final_heat_flux = 7000.0
    initial_excess_heat = 1.3
    final_excess_heat = 5.0
    slope_of_best_fit = log(final_heat_flux/initial_heat_flux)/log(final_excess_heat/initial_excess_heat)
    variable_heat_flux = initial_heat_flux*(variable_excess_heat/initial_excess_heat)**slope_of_best_fit
    print(f"The surface heat flux is approximately {variable_heat_flux:.0f} W/m^2")

# Nucleate boiling stage
if 5.0 <= variable_excess_heat < 30.0:
    initial_heat_flux = 7000.0
    final_heat_flux = 1.5e6
    initial_excess_heat = 5.0
    final_excess_heat = 30.0
    slope_of_best_fit = log(final_heat_flux / initial_heat_flux) / log(final_excess_heat / initial_excess_heat)
    variable_heat_flux = initial_heat_flux * (variable_excess_heat / initial_excess_heat) ** slope_of_best_fit
    print(f"The surface heat flux is approximately {variable_heat_flux:.0f} W/m^2")

# Transition stage
if 30.0 <= variable_excess_heat < 120.:
    initial_heat_flux = 1.5e6
    final_heat_flux = 2.5e4
    initial_excess_heat = 30.0
    final_excess_heat = 120.0
    slope_of_best_fit = log(final_heat_flux / initial_heat_flux) / log(final_excess_heat / initial_excess_heat)
    variable_heat_flux = initial_heat_flux * (variable_excess_heat / initial_excess_heat) ** slope_of_best_fit
    print(f"The surface heat flux is approximately {variable_heat_flux:.0f} W/m^2")

# Film Stage
if 120.0 <= variable_excess_heat < 1200.0:
    initial_heat_flux = 2.5e4
    final_heat_flux = 1.5e6
    initial_excess_heat = 120.0
    final_excess_heat = 1200.0
    slope_of_best_fit = log(final_heat_flux / initial_heat_flux) / log(final_excess_heat / initial_excess_heat)
    variable_heat_flux = initial_heat_flux * (variable_excess_heat / initial_excess_heat) ** slope_of_best_fit
    print(f"The surface heat flux is approximately {variable_heat_flux:.0f} W/m^2")

if variable_excess_heat > 1200:
    print("Surface heat flux is not available")