# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Connor McGuire
# Section:      563
# Assignment:   Lab 1.11
# Date:         5 9 2022

counter = 1
# initializing time window
initial_time = 12
final_time = 85
variable_time = 30.0

# initializing initial x, y, z values
x_initial = 8
y_initial = 6
z_initial = 7

# initializing final x, y, z values
x_final = -5
y_final = 30
z_final = 9

# calculating the slope in each direction x, y, z
x_component_of_slope = (x_final-x_initial)/(final_time-initial_time)
y_component_of_slope = (y_final-y_initial)/(final_time-initial_time)
z_component_of_slope = (z_final-z_initial)/(final_time-initial_time)
while variable_time <= 60:
    # calculating the variable components of direction x, y, z
    variable_x = x_component_of_slope*(variable_time-initial_time)+x_initial
    variable_y = y_component_of_slope*(variable_time-initial_time)+y_initial
    variable_z = z_component_of_slope*(variable_time-initial_time)+z_initial

    # printing variables
    print("At time "+str(variable_time)+ " seconds: ")
    print("x"+str(counter)+" = "+ str(variable_x)+" m")
    print("y"+str(counter)+" = "+ str(variable_y)+" m")
    print("z"+str(counter)+" = "+ str(variable_z)+" m")
    if variable_time < 60:
        print("-----------------------")
    variable_time += 7.5
    counter+=1