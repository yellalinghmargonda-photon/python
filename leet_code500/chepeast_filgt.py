def findCheapestPrice(n: int, flights, src: int, dst: int, k: int) -> int:
    distance = [float('inf')] * n
    distance[src] = 0
    for i in range(k + 1):
        print(f"distance {distance}")
        new_distance = distance[:]
        for u, v, price in flights:
            if distance[u] != float('inf') and distance[u] + price < new_distance[v]:
                new_distance[v] = distance[u] + price
        print(f"new dis {new_distance}")
        distance = new_distance
    return distance[dst] if distance[dst] != float('inf') else -1

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 2
findCheapestPrice(n, flights, src, dst, k)