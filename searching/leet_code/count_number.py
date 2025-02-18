def evenD(number: int)->int:
    count=0
    if number<0:
        number=number*(-1)
    if number==0:
        return False
    while number!=0:
        count+=1
        number=number//10

    if count%2==0:
        return True
    return False

def CountNum(array :list)-> int:
    count=0
    for i in range(len(array)):
        if evenD(array[i]):
           count+=1
    return count

CountNum([22,1,55,6])