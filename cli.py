# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player

def print_board(board):
    for row in board:
        print(" ".join(cell if cell is not None else "-" for cell in row))

def main():
    board = make_empty_board()
    player = 'X'

    while True:
        print_board(board)
        print(f"Player {player}'s turn.")
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        if board[row][col] is not None:
            print("That cell is already occupied. Try again.")
        else:
            board[row][col] = player
            winner = get_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            player = other_player(player)

if __name__ == '__main__':
    main()
