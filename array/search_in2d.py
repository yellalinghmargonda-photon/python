array=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target=5
for j in range(len(array[0])):
    if target>array[0][j]:
        pass
    else:
        break

for i in range(len(array)):
    if target>array[i][0]:
        pass
    else:
        break

print(i,j)
print(array[i][j])

for k in range(i):
    for m in range(j):
       if  array[k][m]==target:
           print('asdsadsadsadsa')
           break
