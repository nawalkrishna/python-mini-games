def check_winner(board, player):
    """Return True if player has three in a row."""
    lines = []
    lines.extend(board)                                                # 3 rows
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])  # 3 columns
    lines.append([board[i][i] for i in range(3)])                      # diagonal \
    lines.append([board[i][2 - i] for i in range(3)])                  # diagonal /

    return any(all(cell == player for cell in line) for line in lines)


def play_game():
    """Play one game. Returns "X", "O", or None for a draw."""
    board = create_board()
    player = "X"

    for _ in range(9):
        print_board(board)
        row, col = get_move(board, player)
        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return player

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")
    return None


def main():
    scores = {"X": 0, "O": 0, "Draws": 0}

    while True:
        winner = play_game()
        if winner:
            scores[winner] += 1
        else:
            scores["Draws"] += 1

        print(f"Score | X: {scores['X']} | O: {scores['O']} | Draws: {scores['Draws']}")

        if input("Play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()