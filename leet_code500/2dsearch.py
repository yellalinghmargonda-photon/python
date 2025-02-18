def exist(board, word):
    def dfs(board, word, index, row, col, visited):
        # If we have matched all characters of the word
        if index == len(word):
            return True

        # Check if the current position is out of bounds or the character doesn't match
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index] or \
                visited[row][col]:
            return False

        # Mark the current cell as visited
        visited[row][col] = True

        # Explore all four possible directions (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            if dfs(board, word, index + 1, row + dr, col + dc, visited):
                return True

        # Backtrack by unmarking the visited cell
        visited[row][col] = False
        return False

    # Create a visited matrix of the same size as the board
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    # Start DFS search from each cell in the grid
    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(board, word, 0, row, col, visited):
                return True

    return False


# Example usage
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"
print(exist(board, word))  # Output: True
