from typing import List
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        # Initialize DP table
        dp = [[float('inf')] * n for _ in range(m)]
        # Base case: first row cost is just grid value
        for col in range(n):
            dp[0][col] = grid[0][col]
        for row in range(1, m):  # Start from the second row
            for col in range(n):  # Current column in this row
                # Try all possible previous columns from row-1
                for prev_col in range(n):
                    prev_value = grid[row - 1][prev_col]  # Value of the previous row cell
                    move_cost = moveCost[prev_value][col]  # Movement cost from prev_col to col

                    # Update DP value for (row, col)
                    dp[row][col] = min(dp[row][col],
                                       dp[row - 1][prev_col] + move_cost + grid[row][col])
        return min(dp[m - 1])
