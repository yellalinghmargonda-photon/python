class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        N = len(grid)
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        # Step 1: Store positions of all steps
        pos = {}
        for i in range(N):
            for j in range(N):
                pos[grid[i][j]] = (i, j)

        # Step 2: Check if the knight starts at (0, 0)
        if pos[0] != (0, 0):
            return False

        # Step 3: Verify each step follows a knight move
        for step in range(1, N * N):
            x1, y1 = pos[step - 1]  # Previous position
            x2, y2 = pos[step]  # Current position

            if (x2 - x1, y2 - y1) not in moves:
                return False

        return True
