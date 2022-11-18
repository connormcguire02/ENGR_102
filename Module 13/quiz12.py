import numpy as np

bingo_board = np.array([['t','e','x','a','s'],
                        ['h','b','r','p','l'],
                        ['y','k','i','q','z'],
                        ['v','o','c','w','d'],
                        ['g','f','m','u','n']])
bingo = [['B',0],['I',1],['N',2],['G',3],['O',4]]

message = 'O1G5G2I1N2O1I1N4N2I1B1G4B2I4I4G2'
decipher = ''

i=0
while i < len(message)-1:
    col = 0
    row = 0
    if message[i] == 'B':
        col = 0
        row = int(message[i+1])-1
    elif message[i] == 'I':
        col = 1
        row = int(message[i+1])-1
    elif message[i] == 'N':
        col = 2
        row = int(message[i+1])-1
    elif message[i] == 'G':
        col = 3
        row = int(message[i+1])-1
    elif message[i] == 'O':
        col = 4
        row = int(message[i+1])-1
    decipher += bingo_board[row][col]
    i += 2
print(decipher)