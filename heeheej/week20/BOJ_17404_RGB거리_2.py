# RGB거리 2
# 115308kb, 136ms
# dp, 첫번째 컬러가 R, G, B일 때 각각의 경우의 수를 나눠서 dp[N-1]를 계산한다.

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')
dp = [[INF]*3 for _ in range(N)]
dp[0] = arr[0]
result = float('inf')
for k in range(3):  # first color
    dp = [[INF]*3 for _ in range(N)]
    dp[0] = arr[0]
    if k == 0:
        dp[1][1] = arr[1][1] + arr[0][0]
        dp[1][2] = arr[1][2] + arr[0][0]
    elif k == 1:
        dp[1][0] = arr[1][0] + arr[0][1]
        dp[1][2] = arr[1][2] + arr[0][1]
    else:
        dp[1][0] = arr[1][0] + arr[0][2]
        dp[1][1] = arr[1][1] + arr[0][2]
    
    for i in range(2, N-1):
        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])

    if k == 0:
        dp[N-1][1] = arr[N-1][1] + min(dp[N-2][0], dp[N-2][2])
        dp[N-1][2] = arr[N-1][2] + min(dp[N-2][0], dp[N-2][1])
    elif k == 1:
        dp[N-1][0] = arr[N-1][0] + min(dp[N-2][1], dp[N-2][2])
        dp[N-1][2] = arr[N-1][2] + min(dp[N-2][0], dp[N-2][1])
    else:
        dp[N-1][0] = arr[N-1][0] + min(dp[N-2][1], dp[N-2][2])
        dp[N-1][1] = arr[N-1][1] + min(dp[N-2][0], dp[N-2][2])
    result = min(result, min(dp[N-1]))

print(result)