from typing import *


def ninjaTraining(n: int, points: List[List[int]]) -> int:
    def ninjapoints(days, last):
        if days == 0:
            max_points = float('-inf')
            for i in range(len(points[0])):
                if i != last:
                    max_points = max(max_points, points[0][i])
            return max_points
        max_points = float('-inf')
        for i in range(3):
            if i != last:
                curr_points = points[days][i] + ninjapoints(days - 1, i)
                max_points = max(max_points, curr_points)
        return max_points

    return ninjaTraining(n - 1, 3)


def ninjapoints_memo(days, last, points, memo):
    if days == 0:
        max_points = float('-inf')
        for i in range(len(points[0])):
            if i != last:
                max_points = max(max_points, points[0][i])
        return max_points
    if (days,last) in memo:
        return memo[(days,last)]
    max_points = float('-inf')
    for i in range(3):
        if i != last:
            curr_points = points[days][i] + ninjapoints_memo(days - 1, i, points,memo)
            max_points = max(max_points, curr_points)
    memo[(days,last)]=max_points
    return max_points
#two d dp as evey day it has 4 possible solutions
def ninjapoints_memo_2d(days, last, points, memo):
        if memo[days][last] != -1:
            return memo[days][last]

        if days == 0:
            max_points = float('-inf')
            for i in range(len(points[0])):
                if i != last:
                    max_points = max(max_points, points[0][i])
            return max_points

        max_points = float('-inf')
        for i in range(3):
            if i != last:
                curr_points = points[days][i] + ninjapoints_memo_2d(days - 1, i, points, memo)
                max_points = max(max_points, curr_points)
        memo[days][last] = max_points
        return max_points

def ninja_tabulation(days, points):
    dp=[[-1]*4 for _ in range(len(days))]
    dp[0][0]=max(points[0][1],points[0][1])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][1], points[0][3])
    dp[0][3] = max(points[0][1], points[0][3], points[0][2])

    for day in range(1, len(points)):
        for last in range(0,4):
            max_points=float('-inf')
            for task in range(4):
                if task != last:
                    curr_points = points[day][task] + dp[days - 1][task]
                    max_points[day][last] = max(max_points[day][last], curr_points)
    return max_points[days-1][3]