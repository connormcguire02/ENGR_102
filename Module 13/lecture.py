# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Project Self-driving Car
# Date:         12/06/22
from project import Path
import turtle

p = Path()

filename = input("Enter the name of the file: ")
directions = open(filename, 'r+')
read = directions.read()
eachdirect = read.split('\n\n')
print(eachdirect)

for direct in eachdirect:
    if 'head' in direct:
        if ' east' in direct:
            p.left(0-Path.p.heading())
        elif 'northeast' in direct:
            p.left(45, )
        elif 'north ' in direct:
            p.left(90, )
        elif 'northwest' in direct:
            p.left(135, )
        elif ' west' in direct:
            p.left(180, )
        elif 'southwest' in direct:
            p.left(225, )
        elif 'south ' in direct:
            p.left(270, )
        else:
            p.left(315, )
    if 'Turn right' in direct:
        p.right(90, )
    if 'Slight right' in direct:
        p.right(45, )
    if 'Turn left' in direct:
        p.left(90, )
    if 'Slight left' in direct:
        p.left(45, )
    if 'Continue' in direct:
        if 'and' not in direct:
            p.forward() # will need distance based on conversions and such
        else:
            pass# harcode
          
    if 'Drive' in direct:
        if 'and' in direct:
            pass# harcode
        elif 'Crow' in direct:
            pass
        else:
            p.forward() # will need distance based on conversions and such
    if 'Take' in direct:
        p.forward()  # will need distance based on conversions and such
    if 'Pass' in direct:
        pass
