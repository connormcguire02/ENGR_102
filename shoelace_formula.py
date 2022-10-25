# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 9.15: Shoelace Formula
# Date:         10/25/22

# Splits the points string up into a list of points
def getpoints(points_string):
    points_list = points_string.split()
    for i in range(len(points_list)):
        points_list[i] = points_list[i].split(',')
        points_list[i][0] = float(points_list[i][0])
        points_list[i][1] = float(points_list[i][1])
    return points_list

# Calculates the cross product of the two inputted points
def cross(point1, point2):
    cross_product = (point1[0] * point2[1]) - (point1[1] * point2[0])
    return cross_product

# Calculates the area of the polygon generated with the list of points
def shoelace(point_list):
    area_sum = 0
    for i in range(len(point_list) - 1):
        area_sum += cross(point_list[i], point_list[i + 1])
    area_sum += cross(point_list[-1], point_list[0])
    return (1 / 2) * area_sum

# Gathers the input and prints the outputted area
def main():
    points = input('Please enter the vertices: ')
    print(f'The area of the polygon is {shoelace(getpoints(points))}')

if __name__ == "__main__":
    main()
