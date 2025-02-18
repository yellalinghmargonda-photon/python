def LinearSearch(array: list , item: int) -> int:

    for i in range(len(array)):
        if array[i]==item:
            return i
    return -1

LinearSearch([],2)
