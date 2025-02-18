def triangular(i, j, grid):
    # Out-of-bounds base case (first!)
    if i >= len(grid) or j >= len(grid[i]):
        return float('inf')  # Large number to prevent choosing invalid paths

    # Actual base case (second)
    if i == len(grid) - 1:
        return grid[i][j]

    # Recursive calls
    down = grid[i][j] + triangular(i + 1, j, grid)
    diagonal = grid[i][j] + triangular(i + 1, j + 1, grid)

    return min(down, diagonal)


# Example
grid = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 1]]
print(triangular(0, 0, grid))  # Output: 12
