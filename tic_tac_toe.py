def create_board():
    return [[" "] * 3 for _ in range(3)]


def print_board(board):
    print()
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()


board = create_board()
board[1][1] = "X"
board[0][2] = "O"
print_board(board)