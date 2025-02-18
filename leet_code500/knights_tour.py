N = 8  # Chessboard size

# All possible moves a Knight can take
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]


def is_valid_move(x, y, board):
    """Check if the move is within bounds and not visited."""
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


def solve_knights_tour():
    """Initializes board and starts the Knight's Tour."""
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Start knight from top-left corner
    board[0][0] = 0

    if not knights_tour(0, 0, 1, board):
        print("Solution does not exist")
        return None
    else:
        print_board(board)
        return board


def knights_tour(x, y, step, board):
    """Recursive function to solve the Knight's Tour problem."""
    if step == N * N:
        return True

    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y, board):
            board[new_x][new_y] = step
            if knights_tour(new_x, new_y, step + 1, board):
                return True
            board[new_x][new_y] = -1  # Backtrack

    return False


def print_board(board):
    """Prints the chessboard with the knight's tour path."""
    for row in board:
        print(" ".join(f"{cell:2}" for cell in row))


# Run the Knight's Tour solution
solve_knights_tour()
