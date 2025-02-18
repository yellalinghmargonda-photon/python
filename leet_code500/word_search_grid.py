def word_search(r,c, i,grid, word, visited):
    if i==len(word):
        return True
        # Boundary & character check
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != word[i] or visited[r][c]:
        return False
    visited[r][c]=True
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for x ,y in directions:
        dr,dc=r+x, c+y
        if word_search(dr, dc,i+1,grid, word, visited):
            return True
    visited[r][c] = False
    return False
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

visited=[[False]* len(board[0]) for _ in range(len(board))]
print(word_search(0,0,0,board,word, visited))
