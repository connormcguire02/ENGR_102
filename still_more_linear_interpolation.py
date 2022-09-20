# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 3.16: Still More Linear Interpolation
# Date:         09/16/22

# Prompting the user for bounds of interpolation
# Prompting inital bound
time_1 = float(input("Enter time 1: "))
#x, y, and z initial are the positions of x, y, and z at time_1
x_initial = float(input("Enter the x position of the object at time 1: "))
y_initial = float(input("Enter the y position of the object at time 1: "))
z_initial = float(input("Enter the z position of the object at time 1: "))
# Prompting the final bound
time_2 = float(input("Enter time 2: "))
#x, y, and z final are the positions of x, y, and z at time_2
x_final = float(input("Enter the x position of the object at time 2: "))
y_final = float(input("Enter the y position of the object at time 2: "))
z_final = float(input("Enter the z position of the object at time 2: "))
#finding slopes using the inputted variables to find the slopes of x, y, and z
x_comp_slope = (x_final - x_initial) / (time_2 - time_1)
y_comp_slope = (y_final - y_initial) / (time_2 - time_1)
z_comp_slope = (z_final - z_initial) / (time_2 - time_1)
# delta t is the variable used to create equal subdivisions between the bounds
delta_t = (time_2 - time_1)/4
# t current is the changing time used to calculate x y z at each time
t_current = time_1
# current x y z are variables used to store interpolated values between the bounds
x_current = (x_comp_slope * (t_current - time_1) + x_initial)
y_current = (y_comp_slope * (t_current - time_1) + y_initial)
z_current = (z_comp_slope * (t_current - time_1) + z_initial)
print(f"At time {t_current:.2f} seconds the object is at ({x_current:.3f}, {y_current:.3f}, {z_current:.3f})")
t_current += delta_t
x_current = (x_comp_slope * (t_current - time_1) + x_initial)
y_current = (y_comp_slope * (t_current - time_1) + y_initial)
z_current = (z_comp_slope * (t_current - time_1) + z_initial)
print(f"At time {t_current:.2f} seconds the object is at ({x_current:.3f}, {y_current:.3f}, {z_current:.3f})")
t_current += delta_t
x_current = (x_comp_slope * (t_current - time_1) + x_initial)
y_current = (y_comp_slope * (t_current - time_1) + y_initial)
z_current = (z_comp_slope * (t_current - time_1) + z_initial)
print(f"At time {t_current:.2f} seconds the object is at ({x_current:.3f}, {y_current:.3f}, {z_current:.3f})")
t_current += delta_t
x_current = (x_comp_slope * (t_current - time_1) + x_initial)
y_current = (y_comp_slope * (t_current - time_1) + y_initial)
z_current = (z_comp_slope * (t_current - time_1) + z_initial)
print(f"At time {t_current:.2f} seconds the object is at ({x_current:.3f}, {y_current:.3f}, {z_current:.3f})")
t_current += delta_t
x_current = (x_comp_slope * (t_current - time_1) + x_initial)
y_current = (y_comp_slope * (t_current - time_1) + y_initial)
z_current = (z_comp_slope * (t_current - time_1) + z_initial)
print(f"At time {t_current:.2f} seconds the object is at ({x_current:.3f}, {y_current:.3f}, {z_current:.3f})")