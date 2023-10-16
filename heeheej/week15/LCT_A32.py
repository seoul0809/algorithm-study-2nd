# 정수 삼각형
# 117036kb, 164ms
# dp문제

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
dp = [[0]*i for i in range(1, N+1)]
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

dp[0][0] = arr[0][0]
for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[N-1]))