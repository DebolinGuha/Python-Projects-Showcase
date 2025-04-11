# tic_tac_toe.py

def print_board(board):
    """Function to print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    """Function to check if the current player has won."""
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    """Function to check if the board is full."""
    return all(all(cell != ' ' for cell in row) for row in board)


def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter row (1, 2, 3): ")) - 1
            col = int(input("Enter column (1, 2, 3): ")) - 1
        except ValueError:
            print("Invalid input. Please enter numbers between 1 and 3.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid move. Please enter numbers between 1 and 3.")
            continue

        if board[row][col] != ' ':
            print("Cell already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()
