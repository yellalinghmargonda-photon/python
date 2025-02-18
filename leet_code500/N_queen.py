def isSafe(row,col, grid):
    for c in range(len(grid[0])):
        if grid[row][c]=='Q':
            return False
    for r in range(len(grid)):
        if grid[r][col] == 'Q':
            return False
    for r, c in zip(range(row-1,-1, -1),range(col-1,-1, -1)):
        if grid[r][c] == 'Q':
            return False
    for r, c in zip(range(row-1,-1, -1),range(col+1,len(grid[0]))):
        if grid[r][c] == 'Q':
            return False
    return  True

def solve(grid, r):
    if r==len(grid):
        return True
    for c in range(len(grid[0])):
        if grid[r][c]=='.':
            if isSafe(r, c, grid):
                grid[r][c]='Q'
                solve(grid, r+1)
                grid[r][c] = '.'

    return False

def isSafe(row,col, grid):
    for c in range(len(grid[0])):
        if grid[row][c]=='Q':
            return False
    for r in range(len(grid)):
        if grid[r][col] == 'Q':
            return False
    for r, c in zip(range(row-1,-1, -1),range(col-1,-1, -1)):
        if grid[r][c] == 'Q':
            return False
    for r, c in zip(range(row-1,-1, -1),range(col+1,len(grid[0]))):
        if grid[r][c] == 'Q':
            return False
    return  True

def solve(row, res, grid):
    if row==len(grid):
        res.append([''.join(row) for row in grid])
        return
    for col in range(len(grid[0])):

            if isSafe(row, col,grid):
                grid[row][col]='Q'
                solve(row+1, res,grid)
                grid[row][col] = '.'
    return
n=4
grid=[['.' for i in range(4)] for _ in range(4)]
res=[]
solve(0, res, grid)
print((res))

