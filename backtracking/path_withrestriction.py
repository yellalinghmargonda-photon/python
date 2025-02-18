def paths(p,maze, r, c):
    if r == len(maze)-1 and c == len(maze[0])-1:
        return [p]

    path_list = []
    if not maze[r][c]:
        return []
    maze[r][c]=False #mark the visited cell as false to avoid revisit
    if r < len(maze)-1:
        path_list.extend(paths(p + 'D', maze,r + 1, c))#going down
    if c < len(maze[0])-1:
        path_list.extend(paths(p + 'R', maze,r, c + 1)) # right
    if r>0 and r < len(maze)-1:
        path_list.extend(paths(p + 'U', maze,r-1,c)) # up
    if c > 0 and r < len(maze[0]) - 1:
        path_list.extend(paths(p + 'L', maze, r, c-1))  #left09   2
    # this line is where the function call is returned revert the changes
    maze[r][c]=True

    return path_list
board=[
    [True,True,True],
    [True,False,True],
    [True,True,True]
]

print(paths('',board,0,0))