# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 3.15: Conversion
# Date:         09/16/22
## To display a specified number of digits after the decimal, use {:.Xf} where X is the number of digits

number = float(input("Please enter the quantity to be converted: "))

#Newtons Conversion 1lb = 4.448N
pounds = number
newtons = pounds * 4.44822271072093
print(f"{pounds:.2f} pounds force is equivalent to {newtons:.2f} Newtons")

#Meters to feet conversion is 1 m = 3.28084 ft
feet = number * 3.28084
print(f"{number:.2f} meters is equivalent to {feet:.2f} feet" )

# Pressure conversion 1 atm = 101.325 kPa
atmospheres = number
kPascals = atmospheres*101.325
print(f"{atmospheres:.2f} atmospheres is equivalent to {kPascals:.2f} kilopascals")

# Watts Conversion: 1 watt = 3.41 btu/hr
watts = (number*3.412141633)
print(f"{number:.2f} watts is equivalent to {watts:.2f} BTU per hour")

#Liters per second to US gallons per minute
#1 L/s = 15.85 G/min due to dimensional analysis
L_per_s = number
G_per_m = L_per_s * 15.85033061
print(f"{L_per_s:.2f} liters per second is equivalent to {G_per_m:.2f} US gallons per minute")

# Celsius to Fahrenheit 32 degree F = (9/5)
celsius = number
fahrenheit = (9/5)*celsius + 32
print(f"{celsius:.2f} degrees Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit")