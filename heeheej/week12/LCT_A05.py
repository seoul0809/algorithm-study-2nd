# 볼링공 고르기

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
weight = list(map(int, input().split()))
arr = [0]*(M+1)

for w in weight:
    arr[w] += 1

result = 0
for i in range(1, M+1):
    N -= arr[i]
    result += arr[i] * N

print(result)


# result = N * (N - 1) // 2
#
# for x in arr:
#     if x > 1:
#         result -= x * (x-1) // 2
# print(result)