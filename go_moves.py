
def display_board(r, c):
    row, col = (9,9)
    board = [[0 for i in range(col)] for j in range(row)]
    board[r][c] = 1
    print(board)
stone_row = int(input('Player 1, input row where you want to place stone: ')) - 1
stone_column = int(input('Player 1, input column where you want to place stone: ')) - 1
display_board(stone_row, stone_column)