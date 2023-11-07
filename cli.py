# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player

def print_board(board):
#Print the Tic-Tac-Toe board
    
    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(cell if cell is not None else ' ' for cell in row)} |")
    print("   0   1   2")

def main():
#Making empty Tic-Tac-Toe board
    
    board = make_empty_board()
    player = 'X'

    while True:
        print_board(board)
        print(f"Player {player}'s turn.")
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Row and column must be 0, 1, or 2.")
            elif board[row][col] is not None:
                print("That cell is already occupied! Try again.")
            else:
                board[row][col] = player
                winner = get_winner(board)
                if winner:
                    print_board(board)
                    print(f"Player {winner} wins!")
                    break
                player = other_player(player)
        except ValueError:
            print("Invalid input! Please enter a number for row and column.")

if __name__ == '__main__':
    main()
