def ZigZAg(text, n):
    matrix=[[] for _ in range(n)]
    down=1
    row=0
    for c in text:
        matrix[row].append(c)
        if row==0:
            down=1
        if row==n-1:
            down=-1
        row+=down
    res=""
    for i in range(n):
        res+="".join(matrix[i])
    print(res)
ZigZAg("PAYPALISHIRING",3)