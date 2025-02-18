def search2DArray(array: list, item: int)->int:
    for i in range(len(array)):
        for j in range(len(array[i])):
            if item==array[i][j]:
                return i,j
    return -1,-1