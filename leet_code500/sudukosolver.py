def issafe(row,col,grid, num):

    for c in range(len(grid[0])):
        if grid[row][c]==num:
            return  False

    for r in range(len(grid)):
        if grid[r][col] == num:
            return False
        # Fix for 3x3 box calculation
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row,box_row+3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == num:
                return False
    return True

def find_empty(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '.':  # Empty cell found
                return (r, c)
    return None  # No empty cells left

def solve(grid):
    empty = find_empty(grid)  # Find the next empty cell
    if not empty:
        return True  # No empty cells left, solution found

    r, c = empty  # Unpack the row and column of the empty cell

    for num in range(1, 10):  # Try numbers 1 to 9
        if issafe(r, c, grid, num):
            grid[r][c] = num  # Place the number

            if solve(grid):  # Recur to solve the next cell
                return True

            grid[r][c] = '.'  # Backtrack if placing `num` didn't lead to a solution

    return False  # No number fits, trigger backtracking
