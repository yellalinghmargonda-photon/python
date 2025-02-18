def paths(p, r, c):
    if r == 1 and c == 1:
        return [p]

    path_list = []
    if r > 1:
        path_list.extend(paths(p + 'V', r - 1, c))
    if c > 1 and r>1:
        path_list.extend(paths(p + 'D', r-1, c - 1))
    if c > 1:
        path_list.extend(paths(p + 'H', r, c - 1))

    return path_list
print(paths('',3,3))