# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 8: Ascii Clock
# Date:         10/22/22

#gathering input
user_im = input("Enter the time: ")
print()
# initializing the clock list that will be mutated throughout the program
clock = []
#adding user input to the clock list
for x in user_im:
    clock.append(x)
#initializing all of the numbers using nested lists
zero = [[0, 0, 0], [0, ' ', 0], [0, ' ', 0], [0, ' ', 0], [0, 0, 0]]
one = [[' ', 1, ' '], [1, 1, ' '], [' ', 1, ' '], [' ', 1, ' '], [1, 1, 1]]
two = [[2, 2, 2], [' ', ' ', 2], [2, 2, 2], [2, ' ', ' '], [2, 2, 2]]
three = [[3, 3, 3], [' ', ' ', 3], [3, 3, 3], [' ', ' ', 3], [3, 3, 3]]
four = [[4, ' ', 4], [4, ' ', 4],  [4, 4, 4], [' ', ' ', 4], [' ', ' ', 4]]
five = [[5, 5, 5], [5, ' ', ' '], [5, 5, 5], [' ', ' ', 5], [5, 5, 5]]
six = [[6, 6, 6], [6, ' ', ' '], [6, 6, 6], [6, ' ', 6], [6, 6, 6]]
seven = [[7, 7, 7], [' ', ' ', 7], [' ', ' ', 7], [' ', ' ', 7], [' ', ' ', 7]]
eight = [[8, 8, 8], [8, ' ', 8], [8, 8, 8], [8, ' ', 8], [8, 8, 8]]
nine = [[9, 9, 9], [9, ' ', 9], [9, 9, 9], [' ', ' ', 9], [9, 9, 9]]
colon = [[' ', ' ', ' '], [' ', ':', ' '], [' ', ' ', ' '], [' ', ':', ' '], [' ', ' ', ' ']]
#setting user input to the number lists using if-elif-else statements
n = 0
while n < len(clock):
    if clock[n] == "1":
        clock[n] = one
    elif clock[n] == "2":
        clock[n] = two
    elif clock[n] == "3":
        clock[n] = three
    elif clock[n] == "4":
        clock[n] = four
    elif clock[n] == "5":
        clock[n] = five
    elif clock[n] == "6":
        clock[n] = six
    elif clock[n] == "7":
        clock[n] = seven
    elif clock[n] == "8":
        clock[n] = eight
    elif clock[n] == "9":
        clock[n] = nine
    elif clock[n] == "0":
        clock[n] = zero
    else:
        clock[n] = colon
    n += 1
#printing out the list of lists using for loops and if-elif-else statements
# since this is a 3-dimensional list, we will need 3 loops
for j in range(5):
    for i in range(len(clock)):
        if len(clock) == 4:
            for k in range(3):
                if i == 2:
                    if k == 2:
                        print(clock[i][j][k], end=' ')
                    else:
                        print(clock[i][j][k], end='')
                elif i == 3:
                    if k == 2:
                        print(clock[i][j][k], end=' ')
                    else:
                        print(clock[i][j][k], end='')
                else:
                    print(clock[i][j][k], end='')
        else:
            for k in range(3):
                if i == 0:
                    if k == 2:
                        print(clock[i][j][k], end=' ')
                    else:
                        print(clock[i][j][k], end='')
                elif i == 3:
                    if k == 2:
                        print(clock[i][j][k], end=' ')
                    else:
                        print(clock[i][j][k], end='')
                elif i == 4:
                    if k == 2:
                        print(clock[i][j][k], end=' ')
                    else:
                        print(clock[i][j][k], end='')
                else:
                    print(clock[i][j][k], end='')
    print()
