def findMissingAndRepeatedValues(grid):
        flattened = []
        for sublist in grid:
            for item in sublist:
                flattened.append(item)
        flattened.sort()
        found=[]
        repeated=[]
        for i in range(1,len(flattened)+1):
            if i==flattened[i]:
                if flattened[i] in found:
                    repeated.append(flattened[i])
                found.append(flattened[i])

            else:
                missing=i
        return repeated.append(missing)



