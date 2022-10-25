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