class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Solves the Sudoku puzzle in place.
        """

        def is_valid(board, row, col, num):
            """
            Check if placing `num` at `board[row][col]` is valid.
            """
            # Check the row
            for j in range(9):
                if board[row][j] == num:
                    return False

            # Check the column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check the 3x3 sub-box
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True

        def backtrack():
            """
            Backtracking function to solve the Sudoku.
            """
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':  # Empty cell
                        for num in map(str, range(1, 10)):  # Numbers '1' to '9'
                            if is_valid(board, i, j, num):
                                board[i][j] = num  # Place the number

                                # Recursively attempt to solve the next cells
                                if backtrack():
                                    return True

                                # Backtrack if the solution doesn't work
                                board[i][j] = '.'

                        return False  # No valid number can be placed here
            return True  # Solved!

        backtrack()
