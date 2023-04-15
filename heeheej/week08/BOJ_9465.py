# 스티커
# 304ms, 170092kb
# dp문제
# 표의 왼쪽부터 오른쪽으로 한 열씩 진행한다
# 0번째 열은 pass, 1번째 열은 자기자신 + 대각선에 있는 값이다.
# 2번쨰 열부터는
# dp[0][i] += max(dp[1][i-1], dp[1][i-2]),
# dp[1][i] += max(dp[0][i-1], dp[0][i-2])가 성립한다.

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1, N):
        if i == 1:
            dp[0][i] += dp[1][i - 1]
            dp[1][i] += dp[0][i - 1]
        else:
            dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][N - 1], dp[1][N - 1]))