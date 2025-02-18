def isSafe(row, col, grid):
    # Check column
    for r in range(len(grid)):
        if grid[r][col] == 'Q':
            return False

    # Check row
    for c in range(len(grid[0])):
        if grid[row][c] == 'Q':
            return False

    # Check left diagonal (\ direction)
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if grid[r][c] == 'Q':
            return False

    # Check right diagonal (/ direction)
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, len(grid[0]))):
        if grid[r][c] == 'Q':
            return False

    return True

def solveNQueens(n, grid, row, solutions):
    if row == n:  # All queens placed successfully
        solutions.append(["".join(r) for r in grid])
        return

    for col in range(n):
        if isSafe(row, col, grid):
            grid[row][col] = 'Q'  # Place queen
            solveNQueens(n, grid, row + 1, solutions)  # Recur for next row
            grid[row][col] = '.'  # Backtrack and remove queen

def nQueens(n):
    grid = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solveNQueens(n, grid, 0, solutions)
    return solutions

# Example usage:
n = 4
result = nQueens(n)
for solution in result:
    for row in solution:
        print(row)
    print()
