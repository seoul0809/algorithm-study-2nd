# 병사 배치하기 (BOJ 18353)
# 114488kb, 148ms
# dp - LIS (가장 긴 증가하는 부분 수열)
# dp[i] = arr[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 0부터 i까지 모든 j에 대하여, dp[i] = max(dp[i], dp[j] + 1) if arr[j] < arr[i]

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1]*N  # 남아있는 병사의 수

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))