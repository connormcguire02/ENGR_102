# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 7: Go Moves
# Date:         10/14/22

# Set board equal to a list of lists
board = [['.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.']]
# Define a function that displays an updated version of the board after every turn
def display_board(r, c, p):
    player_input = 'invalid'
# The arguments are then used to determine which character to place on the index and then replaces the ‘.’ with the
# player's designated character.
    while player_input != 'valid':
        if 0 <= r <= 8 and 0 <= c <= 8:
            if board[r][c] == '.':
                if p == 1: # player 1
                    board[r][c] = chr(9679)
                else: # player 2
                    board[r][c] = chr(9675)
                # the updated board is printed for the next player to choose a spot.
                for i in range(9):
                    for j in range(9):
                        print(f'{board[i][j]}', end=' ')
                    print()
                player_input = 'valid'
            else: # If index already has already been used make the player retry
                print('There is already a stone there, please pick again.')
                r = int(input('Enter new row: ')) - 1
                c = int(input('Enter new column: ')) - 1
        else: # If rows and/or columns are greater than 9 make the player retry
            print('Invalid placement, please pick again.')
            r = int(input('Enter new row: ')) - 1
            c = int(input('Enter new column: ')) - 1
    return()
# print the initial/blank board
for i in range(len(board)):
  for j in range(9):
      print(f'{board[i][j]}', end=' ')
  print()
# check if player wants to play
keep_playing = 'continue' 
# Get input from players
while keep_playing.upper() == 'CONTINUE':
  # prompt the 1st user to choose stone spot
    stone_row = int(input('Player 1, input row where you want to place stone: ')) - 1
    stone_column = int(input('Player 1, input column where you want to place stone: ')) - 1
  # Call the previously defined function using the players row and column inputs as arguments, as well as which player
  # was inputting the numbers
    display_board(stone_row, stone_column, 1)
  # prompt the 2nd user to choose stone spot
    stone_row = int(input('Player 2, input row where you want to place stone: ')) - 1
    stone_column = int(input('Player 2, input column where you want to place stone: ')) - 1
  # Call the previously defined function using the players row and column inputs as arguments, as well as which player
  # was inputting the numbers
    display_board(stone_row, stone_column, 2)
  # Ask for an input to either keep playing or stop the game
    keep_playing = str(input('Would you like to keep playing, please enter continue or stop. '))
print('Thanks for playing!') 
#output if player enters 'stop'