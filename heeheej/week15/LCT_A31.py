# 금광

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    arr = [[] for _ in range(N)]
    for i in range(1, N+1):
        arr[i-1] = temp[M*(i-1):M*i]

    dp = [row[:] for row in arr]
    result = 0
    for y in range(1, M):
        for x in range(N):
            left_up, left, left_down = 0, 0, 0
            if x != 0:
                left_up = dp[x-1][y-1] + arr[x][y]
            if x < N - 1:
                left_down = dp[x+1][y-1] + arr[x][y]
            left = dp[x][y-1] + arr[x][y]
            dp[x][y] = max(dp[x][y], left_up, left, left_down)
            result = max(result, dp[x][y])

    print(result)
